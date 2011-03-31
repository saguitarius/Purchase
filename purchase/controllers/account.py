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
    allow_extra_fields = True
    filter_extra_fields = False
    username = formencode.validators.String(not_empty=True)
    password = formencode.validators.String(not_empty=True)
    
class EditUserForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = False
    password = formencode.validators.String(not_empty=True)
    
class UniqueGroup(formencode.validators.FancyValidator):
    def _to_python(self, values, state):
        users = request.environ['authkit.users']
        available_groups = users.list_groups()
        if request.params['group'] in available_groups:
            raise formencode.Invalid(u'There is group', values, state)
        return values

class AddGroupForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = False
    group = formencode.validators.String(not_empty=True)
    chained_validators = [UniqueGroup()]

class EditGroupForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = False
    group = formencode.validators.String(not_empty=True)  

class AccountController(BaseController):
    
    def index(self):
        "Just redirects to main page of the controlles"
        redirect(url(h.url(controller='account', action='manage_accounts')))

    def signin(self):
        "Sign in"
        '''
        Quite a lot is happening here:
        - adding global variable with user_id for future uses
        - verifying if campaign has started
        - verifying if there's an app for current campaign, if not - create it
        - TODO: something has to be done to previous apps
        - if there's no current campaign, reset global vars
        '''
        if not request.environ.get('REMOTE_USER'):
            # This triggers the AuthKit middleware into displaying the sign-in form
            abort(401)
        else:
            # Identify user uid and put it into global var
            user_q = meta.Session.query(model.User)
            user_id = user_q.filter_by(username = request.environ['REMOTE_USER']).first().uid
            app_globals.user_id = user_id
            
            campaign_q = meta.Session.query(model.Campaign)
            c.current_campaign = campaign_q.filter_by(status = '1').first()
            # Check if there is an active campaign
            if c.current_campaign:
                app_globals.current_campaign_id = c.current_campaign.id
                app_globals.current_campaign_start_date = c.current_campaign.start_date
                app_globals.current_campaign_end_date = c.current_campaign.end_date
                # Check if user has app for this campaign
                app_q = meta.Session.query(model.App)
                c.app = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first()
                try:
                    c.app.id
                # Create app for new campaign
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
                    Have to do something with previous apps!!!
                    '''
            # If none found, reset global vars
            else:
                app_globals.current_campaign_id = 0
                app_globals.current_campaign_start_date = 0
                app_globals.current_campaign_end_date = 0           
            return render('/derived/account/signedin.html')

    def signout(self):
        "Sign out"
        # The actual removal of the AuthKit cookie occurs when the response passes
        # through the AuthKit middleware, we simply need to display a page
        # confirming the user is signed out
        return render('/derived/account/signedout.html')
    
    def signinagain(self):
        "Sign in with other username and password"
        request.environ['paste.auth_tkt.logout_user']()
        return render('/derived/account/signin.html').replace('%s', h.url('signin'))

    def custom_formatter(error):
        return '<span class="error-message">%s</span><br />\n' % (
            htmlfill.html_quote(error)
        )    
    
    @authorize(HasAuthKitRole(['admin']))
    def add_user_form(self):
        "Renders registration form, only Admin should do this"
        users = request.environ['authkit.users']
        c.available_groups = users.list_groups()
        c.available_roles = users.list_roles()
        return render('/derived/account/add_user_form.html')
    
    @authorize(HasAuthKitRole(['admin']))
    @validate(schema=AddUserForm(), form='add_user_form', auto_error_formatter=custom_formatter)
    def add_user(self):
        "Adding new user to the database"
        users = request.environ['authkit.users']
        available_roles = users.list_roles()
        if not users.user_exists(self.form_result['username']):
            users.user_create(self.form_result['username'], password=self.form_result['password'])
            users.user_set_group(self.form_result['username'], self.form_result['group'])
            try:
                for role in self.form_result['roles']:
                    if role not in available_roles:
                        users.user_add_role(self.form_result['username'], self.form_result['roles'])
                    else:
                        users.user_add_role(self.form_result['username'], role)
            except:
                pass
            meta.Session.commit()
            redirect(url(h.url(controller='account', action='manage_accounts')))
        else:
            c.username = self.form_result['username']
            return render('/derived/account/add_user_form.html')
    
    @authorize(HasAuthKitRole(['admin']))
    def edit_user_form(self):
        "Renders registration form, only Admin should do this"
        users = request.environ['authkit.users']
        c.username = request.params['username']
        c.password = users.user_password(request.params['username'])
        c.available_groups = users.list_groups()
        try:
            c.group = users.user_group(request.params['username'])
        except:
            c.group = ''  
        c.available_roles = users.list_roles()
        c.roles = users.user_roles(request.params['username'])
        values = {
            'password': c.password,
            'group': c.group,
            'roles': c.roles,
        }
        return htmlfill.render(render('/derived/account/edit_user_form.html'), values)
    
    @authorize(HasAuthKitRole(['admin']))
    @validate(schema=EditUserForm(), form='edit_user_form', auto_error_formatter=custom_formatter)
    def edit_user(self):
        "Adding new user to the database"
        users = request.environ['authkit.users']
        available_roles = users.list_roles()
        users.user_delete(request.params['username'])
        users.user_create(request.params['username'], password=self.form_result['password'])
        users.user_set_group(request.params['username'], self.form_result['group'])
        try:
            for role in self.form_result['roles']:
                if role not in available_roles:
                    users.user_add_role(request.params['username'], self.form_result['roles'])
                else:
                    users.user_add_role(request.params['username'], role)
        except:
            pass
        meta.Session.commit()
        redirect(url(h.url(controller='account', action='manage_accounts')))
    
    @authorize(HasAuthKitRole(['admin']))
    def delete_user(username):
        "Deletes user from datebase. Need acknowledgement here with JS!!!"
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
        users = request.environ['authkit.users']
        users.group_create(request.params['group'])
        redirect(url(h.url(controller='account', action='manage_accounts')))
    
    @authorize(HasAuthKitRole(['admin']))
    def edit_group_form(self):
        users = request.environ['authkit.users']
        c.group = request.params['group']
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
        }        
        return htmlfill.render(render('/derived/account/edit_group_form.html'), values)
    
    @authorize(HasAuthKitRole(['admin']))
    @validate(schema=EditGroupForm(), form='edit_group_form', auto_error_formatter=custom_formatter)
    def edit_group(self):
        users = request.environ['authkit.users']
        # Change group name
        if self.form_result['group'] != request.params['group']:
            users.group_create(self.form_result['group'])
            for user in users.list_users():
                if users.user_has_group(user, request.params['group']):
                    users.user_remove_group(user)
                    users.user_set_group(user, self.form_result['group'])
            users.group_delete(request.params['group'])
        # Change group boss
        if not users.user_has_role(self.form_result['boss'], 'boss'):
            # Create list of users in group
            users_in_group_list = []
            for user in users.list_users():
                if users.user_has_group(user, request.params['group']):
                    try:
                        users_in_group_list += [user]
                    except:
                        pass       
            # Remove old boss and add new boss
            for user in users_in_group_list:
                if users.user_has_role(user, 'boss'):
                    users.user_remove_role(user, 'boss')
            users.user_add_role(self.form_result['boss'], 'boss')
                    
        redirect(url(h.url(controller='account', action='manage_accounts')))
    
    @authorize(HasAuthKitRole(['admin']))
    def delete_group(self):
        users = request.environ['authkit.users']
        for user in users.list_users():
            # Remove users from unexisting group
            if users.user_has_group(user, request.params['group']):
                users.user_remove_group(user)
            # Remove Boss role from boss of unexisting group
            if users.user_has_role(user, 'boss'):
                users.user_remove_role(user, 'boss')
        users.group_delete(request.params['group'])
        redirect(url(h.url(controller='account', action='manage_accounts')))
    
    @authorize(HasAuthKitRole(['admin']))
    def manage_accounts(self):
        "Creating and editing user data, groups and roles."
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
