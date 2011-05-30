## -*- coding: utf-8 -*-

import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from purchase.lib.base import BaseController, render

import purchase.lib.helpers as h

from purchase.lib import auth
from authkit.users.sqlalchemy_driver import UsersFromDatabase
from authkit.authorize.pylons_adaptors import authorize
from authkit.authorize.pylons_adaptors import authorized
from authkit.permissions import ValidAuthKitUser
from authkit.permissions import HasAuthKitRole

from purchase.model import meta
from pylons import request
import purchase.model as model

from pylons.decorators import validate

import formencode
from formencode import htmlfill
from formencode.schema import Schema
from formencode.validators import Invalid, FancyValidator
from formencode.validators import Int, DateConverter, String, OneOf
from formencode import variabledecode
from formencode.foreach import ForEach
from formencode.api import NoDefault

from pylons import app_globals
import datetime

log = logging.getLogger(__name__)

class AddUserForm(formencode.Schema):
    """Проверка данных формы добавления новой учётной записи пользователя"""
    allow_extra_fields = True
    filter_extra_fields = False
    username = formencode.validators.PlainText(
        not_empty=True,
        messages={
            'empty':u'Введите логин.',
            'invalid':u'Логин может содержать только символы латинского алфавита, цифры и знак "_"'
        })
    view = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':u'Введите имя.',
        })
    mail = formencode.validators.Email(
        not_empty=True,
        messages={
            'empty':u'Введите e-mail.',
            'noAt':u'E-mail должен быть вида mail@example.com',
            'badUsername': u'Неправильно введено имя (часть до @: %(username)s)',
            'badDomain': u'Домен введён неверно (часть после @: %(domain)s)',
            'domainDoesNotExist': u'Домен не существует (часть после @: %(domain)s)',
        })
    password = formencode.validators.PlainText(
        not_empty=True,
        messages={
            'empty':u'Введите пароль.',
            'invalid':u'Пароль может содержать только символы латинского алфавита, цифры и знак "_"'
        })
    
class EditUserForm(formencode.Schema):
    """Проверка данных формы изменения учётной записи пользователя"""
    allow_extra_fields = True
    filter_extra_fields = False
    view = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':u'Введите имя.',
        })
    mail = formencode.validators.Email(
        not_empty=True,
        messages={
            'empty':u'Введите e-mail.',
            'noAt':u'E-mail должен быть вида mail@example.com',
            'badUsername': u'Неправильно введено имя (часть до @: %(username)s)',
            'badDomain': u'Домен введён неверно (часть после @: %(domain)s)',
            'domainDoesNotExist': u'Домен не существует (часть после @: %(domain)s)',
        })
    password = formencode.validators.PlainText(
        not_empty=True,
        messages={
            'empty':u'Введите пароль.',
            'invalid':u'Пароль может содержать только символы латинского алфавита, цифры и знак "_"'
        })
    
class UniqueGroup(formencode.validators.FancyValidator):
    """Проверка, уникально ли название группы"""
    def _to_python(self, values, state):
        users = request.environ['authkit.users']
        available_groups = users.list_groups()
        if request.params['group'] in available_groups:
            raise formencode.Invalid(u'There is group', values, state)
        return values

class AddGroupForm(formencode.Schema):
    """Проверка данных формы добавления новой группы"""
    allow_extra_fields = True
    filter_extra_fields = False
    group = formencode.validators.PlainText(
        not_empty=True,
        messages={
            'empty':u'Введите название группы.',
            'invalid':u'Название группы может содержать только символы латинского алфавита, цифры и знак "_"'
        })
    view = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':u'Введите название группы для отображения.',
        })
    chained_validators = [UniqueGroup()]

class EditGroupForm(formencode.Schema):
    """Проверка данных формы изменения параметров"""
    allow_extra_fields = True
    filter_extra_fields = False
    group = formencode.validators.PlainText(
        not_empty=True,
        messages={
            'empty':u'Введите название группы.',
            'invalid':u'Название группы может содержать только символы латинского алфавита, цифры и знак "_"'
        }) 
    view = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':u'Введите название группы для отображения.',
        })

class AccountController(BaseController):
    
    def index(self):
        """Перенаправление на главную страницу контроллера"""
        redirect(url(h.url(controller='account', action='manage_accounts')))

    def signin(self):
        """Вход в систему
        Здесь происходит много всего:
        - добавление глобальной переменной, содержащей user_id
        - проверка, началась ли кампания
        - проверка, создана ли заявка для текущей кампании; если нет - создание
        - если кампания не запущена, сбросить глобальные переменные
        - TODO: что-то надо сделать с предыдущими заявками"""
        if not request.environ.get('REMOTE_USER'):
            # This triggers the AuthKit middleware into displaying the sign-in form
            abort(401)
        else:
            # Определить uis пользователя и поместить в глобальную переменную
            user_q = meta.Session.query(model.User)
            user = user_q.filter_by(username = request.environ['REMOTE_USER']).first()
            app_globals.user_id = user.uid
            app_globals.user_group = user.group.view
            app_globals.user_view = user.view
            
            campaign_q = meta.Session.query(model.Campaign)
            c.current_campaign = campaign_q.filter_by(status = '1').first()
            # Проверить, есть ли активные кампании
            if c.current_campaign:
                app_globals.current_campaign_id = c.current_campaign.id
                app_globals.current_campaign_start_date = c.current_campaign.start_date
                app_globals.current_campaign_end_date = c.current_campaign.end_date
                # Проверить, есть ли у пользователя заявка для этой кампании
                app_q = meta.Session.query(model.App)
                c.app = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first()
                try:
                    c.app.id
                # Создать заявка для новой кампании
                except:
                    app = model.App()
                    app.author_id = app_globals.user_id
                    app.status = '1'
                    app.campaign_id = app_globals.current_campaign_id
                    app.created = datetime.datetime.now()
                    app.edited = datetime.datetime.now()
                    meta.Session.add(app)
                    meta.Session.flush()
                    '''
                    Сделать что-то с предыдущими заявками!!!
                    '''
            # Если кампаний не найдено, обнулить глобальные переменные
            else:
                #app_globals.current_campaign_id = 0
                #app_globals.current_campaign_start_date = 0
                #app_globals.current_campaign_end_date = 0 
                pass          
            return render('/derived/account/signedin.html')

    def signout(self):
        """Выход из системы"""
        # The actual removal of the AuthKit cookie occurs when the response passes
        # through the AuthKit middleware, we simply need to display a page
        # confirming the user is signed out
        return render('/derived/account/signedout.html')
    
    def signinagain(self):
        """Вход в системe с другими логином и паролем"""
        request.environ['paste.auth_tkt.logout_user']()
        return render('/derived/account/signin.html').replace('%s', h.url('signin'))

    def custom_formatter(error):
        return '<span class="error-message">%s</span><br />\n' % (
            htmlfill.html_quote(error)
        )    
    
    @authorize(HasAuthKitRole(['admin']))
    def add_user_form(self):
        """Показывает форму регистрации, только Администратор должен иметь доступ к ней"""
        users = request.environ['authkit.users']
        #c.available_groups = users.list_groups()[1:]
        groups_q = meta.Session.query(model.Group)    
        c.available_groups = [(group.name, group.view) for group in groups_q]
        #c.available_roles = users.list_roles()
        return render('/derived/account/add_user_form.html')
    
    @authorize(HasAuthKitRole(['admin']))
    @validate(schema=AddUserForm(), form='add_user_form', auto_error_formatter=custom_formatter)
    def add_user(self):
        """Добавление нового пользователя"""
        users = request.environ['authkit.users']
        c.available_groups = users.list_groups()[1:]
        available_roles = users.list_roles()
        if not users.user_exists(self.form_result['username']):
            users.user_create(self.form_result['username'], password=self.form_result['password'])
            users.user_set_view(self.form_result['username'], self.form_result['view'])
            users.user_set_mail(self.form_result['username'], self.form_result['mail'])
            users.user_set_group(self.form_result['username'], self.form_result['group'])
#            try:
#                for role in self.form_result['roles']:
#                    if role not in available_roles:
#                        users.user_add_role(self.form_result['username']), self.form_result['roles'])
#                    else:
#                        users.user_add_role(self.form_result['username']), role)
#            except:
#                pass
            users.user_add_role(self.form_result['username'], 'user')
            meta.Session.commit()
            redirect(url(h.url(controller='account', action='manage_accounts')))
        else:
            c.username = self.form_result['username']
            return render('/derived/account/add_user_form.html')
    
    @authorize(HasAuthKitRole(['admin']))
    def edit_user_form(self):
        """Показывает форму регистрации, только Администратор должен иметь доступ к ней"""
        users = request.environ['authkit.users']
        c.username = request.params['username']
        c.password = users.user_password(c.username)
        c.view = (users.user_view(c.username))
        c.mail = (users.user_mail(c.username))
        #c.available_groups = users.list_groups()[1:]
        groups_q = meta.Session.query(model.Group)    
        c.available_groups = [(group.name, group.view) for group in groups_q]
        try:
            c.group = users.user_group(request.params['username'])
        except:
            c.group = ''  
        #c.available_roles = users.list_roles()
#       c.roles = users.user_roles(request.params['username'])
        values = {
            'password': c.password,
            'group': c.group,
            'mail': c.mail,
            'view': c.view,
#            'roles': c.roles,
        }
        return htmlfill.render(render('/derived/account/edit_user_form.html'), values)
    
    @authorize(HasAuthKitRole(['admin']))
    @validate(schema=EditUserForm(), form='edit_user_form', auto_error_formatter=custom_formatter)
    def edit_user(self):
        """Изменение параметов учётной записи пользователя"""
        users = request.environ['authkit.users']
        #available_roles = users.list_roles()
        try:
            user_role = users.user_roles(request.params['username'])[0]
        except:
            user_role = 'user'
        users.user_set_password(request.params['username'], self.form_result['password'])
        users.user_set_view(request.params['username'], self.form_result['view'])
        users.user_set_mail(request.params['username'], self.form_result['mail'])        
        users.user_set_group(request.params['username'], self.form_result['group'])
        users.user_add_role(request.params['username'], user_role)
#        try:
#            for role in self.form_result['roles']:
#                if role not in available_roles:
#                    users.user_add_role(request.params['username'], self.form_result['roles'])
#                else:
#                    users.user_add_role(request.params['username'], role)
#        except:
#            pass
        meta.Session.commit()
        redirect(url(h.url(controller='account', action='manage_accounts')))
    
    @authorize(HasAuthKitRole(['admin']))
    def delete_user(username):
        """Удаление пользователя"""
        users = request.environ['authkit.users']
        if request.params['username'] == 'admin':
            # Javascript here!
            redirect(url(h.url(controller='account', action='manage_accounts')))
        else:
            users.user_delete(request.params['username'])
        redirect(url(h.url(controller='account', action='manage_accounts')))
    
    @authorize(HasAuthKitRole(['admin']))
    @validate(schema=AddGroupForm(), form='manage_accounts', auto_error_formatter=custom_formatter)
    def add_group(self):
        """Добавление группы"""
        users = request.environ['authkit.users']
        users.group_create(request.params['group'])
        redirect(url(h.url(controller='account', action='manage_accounts')))
    
    @authorize(HasAuthKitRole(['admin']))
    def edit_group_form(self):
        """Форма изменения параметров группы"""
        users = request.environ['authkit.users']
        c.group = request.params['group']
        c.group_view = users.group_view(c.group)
        users_in_group_list = []
        for user in users.list_users():
            if users.user_has_group(user, request.params['group']):
                try:
                    users_in_group_list += [user]
                except:
                    pass
                if users.user_has_role(user, 'boss'):
                    c.boss = user
                else:
                    c.boss = ''
        c.users_in_group_list = users_in_group_list
        values = {
            'group': c.group,
            'view': c.group_view,
        }        
        return htmlfill.render(render('/derived/account/edit_group_form.html'), values)
    
    @authorize(HasAuthKitRole(['admin']))
    @validate(schema=EditGroupForm(), form='edit_group_form', auto_error_formatter=custom_formatter)
    def edit_group(self):
        """Изменение параметров группы"""
        users = request.environ['authkit.users']
        # Изменение названия группы
        if self.form_result['group'] != request.params['group']:
            users.group_create(self.form_result['group'])
            for user in users.list_users():
                if users.user_has_group(user, request.params['group']):
                    users.user_remove_group(user)
                    users.user_set_group(user, self.form_result['group'])
            users.group_delete(request.params['group'])
        # Изменение ответственного по группе
        if not users.user_has_role(self.form_result['boss'], 'boss'):
            # Создание списка пользователей группы
            users_in_group_list = []
            for user in users.list_users():
                if users.user_has_group(user, request.params['group']):
                    try:
                        users_in_group_list += [user]
                    except:
                        pass       
            # Удаление старого ответственного по группе и назначение нового
            for user in users_in_group_list:
                if users.user_has_role(user, 'boss'):
                    users.user_remove_role(user, 'boss')
            users.user_add_role(self.form_result['boss'], 'boss')
        users.group_set_view(self.form_result['group'], self.form_result['view'])            
        redirect(url(h.url(controller='account', action='manage_accounts')))
    
    @authorize(HasAuthKitRole(['admin']))
    def delete_group(self):
        """Удаление группы"""
        users = request.environ['authkit.users']
        for user in users.list_users():
            # Перемещение пользователей из несуществующей группы
            if users.user_has_group(user, request.params['group']):
                users.user_remove_group(user)
            # Удаление права отстветственного несуществующей группы
            if users.user_has_role(user, 'boss'):
                users.user_remove_role(user, 'boss')
        users.group_delete(request.params['group'])
        redirect(url(h.url(controller='account', action='manage_accounts')))
    
    @authorize(HasAuthKitRole(['admin']))
    def manage_accounts(self):
        """Основная страница управления пользователями
        Список пользователей, групп"""
        users = request.environ['authkit.users']
        boss_list = {}
        c.users = users
        for user in users.list_users():
            if users.user_has_role(user, 'boss'):
                try:
                    boss_list.update({users.user_group(user):user})
                except:
                    pass
        c.boss_list = boss_list
        return render('/derived/account/manage_accounts.html')
