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

import purchase.model as model
import purchase.model.meta as meta

import formencode
from formencode import htmlfill
from formencode.foreach import ForEach
from pylons.decorators import validate
from pylons.decorators.rest import restrict
from sqlalchemy import delete
from sqlalchemy.orm import aliased
from sqlalchemy.sql import and_, or_, not_
import datetime

from pylons import app_globals

import smtplib

log = logging.getLogger(__name__)

class App_Element(formencode.Schema):
    """Проверка данных формы заявки"""
    quarter1 = formencode.validators.Int(not_empty=True)
    quarter2 = formencode.validators.Int(not_empty=True)
    quarter3 = formencode.validators.Int(not_empty=True)
    quarter4 = formencode.validators.Int(not_empty=True)
    finsource = formencode.validators.String(not_empty=True)
    needs = formencode.validators.String(not_empty=True)
    place = formencode.validators.String(not_empty=True)
    
class SaveApp(formencode.Schema):
    """Проверка всех элементов заявки"""
    allow_extra_fields = True
    filter_extra_fields = False
    app_element = ForEach(App_Element)
    
class SaveGroupApp(formencode.Schema):
    """Проверка данных формы сохранения заявки по отделу"""
    allow_extra_fields = True
    filter_extra_fields = False
    quarter1 = formencode.validators.Int(not_empty=True)
    quarter2 = formencode.validators.Int(not_empty=True)
    quarter3 = formencode.validators.Int(not_empty=True)
    quarter4 = formencode.validators.Int(not_empty=True)
    finsource = formencode.validators.String(not_empty=True)
    needs = formencode.validators.String(not_empty=True)
    place = formencode.validators.String(not_empty=True)

class AppController(BaseController):
    
    """Статусы заявки:
        1 Создана, может быть изменена автором
        2 Отправлена ответственному по отделу на рассмотрение, 
            не может быть изменена автором
        3 Проверена ответственным по отделу и отправлена ответственному по
            предприятию, не может быть изменена автором
        4 Утверждена ответственным по предприятию
    """
    
    """Статусы элементов заявок:
        0 Не изменялось
        --Согласование--
        1 Параметры изменены ответственным по отделу
        2 Объект заменён на другой ответственным по отделу
        3 Объект удалён ответственным по отделу
        4 Утверждён ответственным по предприятию
        --Реализация--
        5 Закуплено
        6 Закуплено, изменены параметры
        7 Закуплено, заменён объект
        8 Не закуплено
    """
    
    @authorize(ValidAuthKitUser())
    def __before__(self):
        """
            Проверки для инициализации глобальных переменных
        """
        # Определить uid пользователя и поместить в глобальную переменную
        user_q = meta.Session.query(model.User)
        user = user_q.filter_by(username = request.environ['REMOTE_USER']).first()
        app_globals.user_id = user.uid
        app_globals.user_group = user.group.view
        app_globals.user_view = user.view
            
        campaign_q = meta.Session.query(model.Campaign)
        c.current_campaign = campaign_q.filter_by(status = '1').first()
        # Проверить, есть ли запущенная кампания
        if c.current_campaign:
            app_globals.current_campaign_id = c.current_campaign.id
            app_globals.current_campaign_start_date = c.current_campaign.start_date
            app_globals.current_campaign_end_date = c.current_campaign.end_date     
            
        c.finished_active_campaign = campaign_q.filter_by(status = '2').first()
        # Проверить, есть ли завершённая активная кампания
        if c.finished_active_campaign:
            app_globals.current_campaign_id = c.finished_active_campaign.id
            app_globals.current_campaign_start_date = c.finished_active_campaign.start_date
            app_globals.current_campaign_end_date = c.finished_active_campaign.end_date    
            
            app_globals.finished_active_campaign_id = c.finished_active_campaign.id
            app_globals.finished_active_campaign_start_date = c.finished_active_campaign.start_date
            app_globals.finished_active_campaign_end_date = c.finished_active_campaign.end_date       
    
    @authorize(ValidAuthKitUser())
    def user_app(self):
        """Вывод данных о заявке пользователя"""
        # Выбор заявки и элементов заявки для определённого пользователя
        app_q = meta.Session.query(model.App)
        c.current_app = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first()   
        app_elements_q = meta.Session.query(model.AppElements)
        c.current_app_elements = app_elements_q.filter_by(app_id = c.current_app.id)
        
        # Выбор всех доступных вариантов источников финансирования и нужд
        finsource_q = meta.Session.query(model.FinSource)
        c.available_finsource = [(finsource.id, finsource.name) for finsource in finsource_q]     
        needs_q = meta.Session.query(model.Needs)
        c.available_needs = [(needs.id, needs.name) for needs in needs_q]
        users = request.environ['authkit.users']
        
        # c.available_groups = users.list_groups()  
        groups_q = meta.Session.query(model.Group)    
        c.available_groups = [(group.uid, group.view) for group in groups_q]
        
        # Информациия о заявке           
        values = {}
        element_amount = {}
        element_amountp = {}
        element_price = {}
        element_pricep = {}
        total_price = 0
        total_pricep = 0
        for element in c.current_app_elements:
            values['quarter1_el'+str(element.id)] = element.quarter1
            values['quarter2_el'+str(element.id)] = element.quarter2
            values['quarter3_el'+str(element.id)] = element.quarter3
            values['quarter4_el'+str(element.id)] = element.quarter4
            values['amountp_el'+str(element.id)] = element.amountp
            values['pricep_el'+str(element.id)] = element.pricep
            values['finsource_el'+str(element.id)] = element.finsource
            values['needs_el'+str(element.id)] = element.needs
            values['place_el'+str(element.id)] = element.place
            values['note_el'+str(element.id)] = element.note
            
            element_amount[element.id] = element.quarter1 + element.quarter2 + element.quarter3 + element.quarter4
            element_amountp[element.id] = element.amountp
            element_pricep[element.id] = element.pricep
            element_price[element.id] = element_amount[element.id] * element.items.price
            if element.status == 3:
                pass
            else:
                total_price += element_price[element.id]
                total_pricep += element_pricep[element.id]
        
        c.element_amount = element_amount
        c.element_amountp = element_amountp
        c.element_price = element_price  
        c.element_pricep = element_pricep  
        c.total_price = total_price
        c.total_pricep = total_pricep
        
        c.all_apps = app_q.filter_by(author_id = app_globals.user_id).all()
        
        return htmlfill.render(render('/derived/app/user_view.html'), values)
    
    @authorize(ValidAuthKitUser())
    def user_app_print(self):
        """Заявка пользователя - версия для печати"""
        #response.content_type = 'application/download'
        
        # Выбор заявки и элементов заявки для определённого пользователя
        app_q = meta.Session.query(model.App)
        c.current_app = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first()   
        app_elements_q = meta.Session.query(model.AppElements)
        c.current_app_elements = app_elements_q.filter_by(app_id = c.current_app.id)
        
        # Выбор всех доступных вариантов источников финансирования и нужд
        finsource_q = meta.Session.query(model.FinSource)
        c.available_finsource = [(finsource.id, finsource.name) for finsource in finsource_q]     
        needs_q = meta.Session.query(model.Needs)
        c.available_needs = [(needs.id, needs.name) for needs in needs_q]
        users = request.environ['authkit.users']
        
        # c.available_groups = users.list_groups()  
        groups_q = meta.Session.query(model.Group)    
        c.available_groups = [(group.uid, group.view) for group in groups_q]
        
        # Информациия о заявке           
        values = {}
        element_amount = {}
        element_amountp = {}
        element_price = {}
        element_pricep = {}
        total_price = 0
        total_pricep = 0
        for element in c.current_app_elements:
            values['quarter1_el'+str(element.id)] = element.quarter1
            values['quarter2_el'+str(element.id)] = element.quarter2
            values['quarter3_el'+str(element.id)] = element.quarter3
            values['quarter4_el'+str(element.id)] = element.quarter4
            values['amountp_el'+str(element.id)] = element.amountp
            values['pricep_el'+str(element.id)] = element.pricep
            values['finsource_el'+str(element.id)] = element.finsource
            values['needs_el'+str(element.id)] = element.needs
            values['place_el'+str(element.id)] = element.place
            values['note_el'+str(element.id)] = element.note
            
            element_amount[element.id] = element.quarter1 + element.quarter2 + element.quarter3 + element.quarter4
            element_amountp[element.id] = element.amountp
            element_pricep[element.id] = element.pricep
            element_price[element.id] = element_amount[element.id] * element.items.price
            if element.status == 3:
                pass
            else:
                total_price += element_price[element.id]
                total_pricep += element_pricep[element.id]
        
        c.element_amount = element_amount
        c.element_amountp = element_amountp
        c.element_price = element_price  
        c.element_pricep = element_pricep  
        c.total_price = total_price
        c.total_pricep = total_pricep
        
        c.all_apps = app_q.filter_by(author_id = app_globals.user_id).all()
        
        # Текущий год
        c.year = datetime.datetime.now().strftime('%Y')
        
        return htmlfill.render(render('/derived/app/user_view_print.html'), values)
    
    @authorize(ValidAuthKitUser())
    def add_item(self):
        """Добавление нового объекта в заявку"""
        app_q = meta.Session.query(model.App)
        c.current_app = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first()
        if (c.current_app.status == 1) or (h.auth.authorized(h.auth.is_valid_user)):    
            app_elements_q = meta.Session.query(model.AppElements)
            # Проверка, есть ли уже этот элемент в заявке
            c.repeat_element = app_elements_q.filter_by(app_id = c.current_app.id).filter_by(item_id = request.urlvars['id']).first()
            try:
                c.repeat_element.id
            except:
                app_elements = model.AppElements()
                app_elements.app_id = c.current_app.id
                app_elements.item_id = request.urlvars['id']
                app_elements.quarter1 = '0'
                app_elements.quarter2 = '0'
                app_elements.quarter3 = '0'
                app_elements.quarter4 = '0'
                app_elements.quarter1p = '0'
                app_elements.quarter2p = '0'
                app_elements.quarter3p = '0'
                app_elements.quarter4p = '0'
                app_elements.amount = '0'
                app_elements.amountp = '0'
                app_elements.price = '0'
                app_elements.pricep = '0'
                app_elements.finsource = '1'
                app_elements.needs = '1'
                app_elements.place = '1'
                app_elements.note = u' '
                app_elements.status = '0'
                meta.Session.add(app_elements)
                meta.Session.flush() 
        else:
            # Javasctipt here
            pass
        
        h.redirect(url(controller='catalog', action='section', id=app_globals.current_section_id))
    
    @authorize(ValidAuthKitUser())        
    def delete_item(self):
        """Удаление объекта из заявки"""
        app_elements_q = meta.Session.query(model.AppElements)
        app_element = app_elements_q.filter_by(id = request.urlvars['id']).first()
        meta.Session.delete(app_element)
        meta.Session.commit()
        h.redirect(url(controller='app', action='user_app'))
    
    @authorize(ValidAuthKitUser())
    @validate(schema=SaveApp(), form='user_app')    
    def save_user_app(self):
        """Сохранение изменений, внесённых в заявку пользователя"""
        app_q = meta.Session.query(model.App)
        current_app = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first() 
        app_elements_q = meta.Session.query(model.AppElements)
        current_app_elements = app_elements_q.filter_by(app_id = current_app.id)
        
        for element in current_app_elements:
            element.quarter1 = self.form_result[u'quarter1_el'+str(element.id)]
            element.quarter2 = self.form_result[u'quarter2_el'+str(element.id)]
            element.quarter3 = self.form_result[u'quarter3_el'+str(element.id)]
            element.quarter4 = self.form_result[u'quarter4_el'+str(element.id)]
            element.amount = int(element.quarter1) + int(element.quarter2) + int(element.quarter3) + int(element.quarter4)
            element.price = int(element.amount) * int(element.items.price)
            element.finsource = self.form_result[u'finsource_el'+str(element.id)]
            element.needs = self.form_result[u'needs_el'+str(element.id)]
            element.place = self.form_result[u'place_el'+str(element.id)]
            element.note = self.form_result[u'note_el'+str(element.id)]
            meta.Session.commit()
        
        h.redirect(url(controller='app', action='user_app'))
    
    @authorize(ValidAuthKitUser())    
    def app_to_boss(self):
        """Передача заявки пользователя ответственному по отделу"""
        # Пользователять отправляет заявку ответственному по отделу
        app_q = meta.Session.query(model.App)
        current_app = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first() 
        if current_app.status == 1:
            current_app.status = 2 # Передача заявки ответственному по отделу
        meta.Session.commit()
        h.redirect(url(controller='app', action='user_app'))
    
    @authorize(HasAuthKitRole(['boss']))    
    def group_app(self): 
        """Вывод данных о заявке по отделу"""
        # Пустой запрос
        group_app_elements = meta.Session.query(model.AppElements).filter_by(id = 0)
        # Выбор группы
        boss_q = meta.Session.query(model.User)
        boss_group = boss_q.filter_by(username = request.environ['REMOTE_USER']).first().group_uid
        c.boss_group_view = boss_q.filter_by(username = request.environ['REMOTE_USER']).first().group.view
        # Выбор пользователей в этой группе
        users_q = meta.Session.query(model.User)
        users_in_group = users_q.filter_by(group_uid = boss_group).all()
        
        # Выбор заявки и элементов заявок, соответстующих определённой группе
        for user in users_in_group:       
            app_q = meta.Session.query(model.App)
            current_app = app_q.filter_by(author_id = user.uid).filter_by(campaign_id = app_globals.current_campaign_id) 
            current_app = current_app.filter(or_(model.App.status.like(2), model.App.status.like(3))).first()  
            app_elements_q = meta.Session.query(model.AppElements)
            try:
                current_app_elements = app_elements_q.filter_by(app_id = current_app.id)
                group_app_elements = group_app_elements.union(current_app_elements) 
            except:
                pass     
        c.group_app_elements = group_app_elements.order_by(model.AppElements.item_id.asc())
        
        total_price = 0
        for app_element in c.group_app_elements:
            if app_element.status == 3:
                pass
            else:
                total_price += app_element.price
        c.total_price = total_price
        
        # Вывод корректных названий групп
        groups_q = meta.Session.query(model.Group)    
        c.available_groups = [(group.uid, group.view) for group in groups_q]
        
        # Вывод информации о лимитах
        users = request.environ['authkit.users']
        limit_q = meta.Session.query(model.Limit)
        try:
            c.limit = limit_q.filter_by(campaign_id = app_globals.current_campaign_id).filter_by(group_uid = boss_group).first()
        except:
            c.limit = '0'
        
        return render('/derived/app/group_view.html')
    
    @authorize(HasAuthKitRole(['boss']))    
    def group_app_print(self): 
        """Вывод данных о заявке по отделу - версия для печати"""
        #response.content_type = 'application/download'
        
        # Пустой запрос
        group_app_elements = meta.Session.query(model.AppElements).filter_by(id = 0)
        # Выбор группы
        boss_q = meta.Session.query(model.User)
        boss_group = boss_q.filter_by(username = request.environ['REMOTE_USER']).first().group_uid
        c.boss_group_view = boss_q.filter_by(username = request.environ['REMOTE_USER']).first().group.view
        # Выбор пользователей в этой группе
        users_q = meta.Session.query(model.User)
        users_in_group = users_q.filter_by(group_uid = boss_group).all()
        
        # Выбор заявки и элементов заявок, соответстующих определённой группе
        for user in users_in_group:       
            app_q = meta.Session.query(model.App)
            current_app = app_q.filter_by(author_id = user.uid).filter_by(campaign_id = app_globals.current_campaign_id) 
            current_app = current_app.filter(or_(model.App.status.like(2), model.App.status.like(3))).first()  
            app_elements_q = meta.Session.query(model.AppElements)
            try:
                current_app_elements = app_elements_q.filter_by(app_id = current_app.id)
                group_app_elements = group_app_elements.union(current_app_elements) 
            except:
                pass     
        c.group_app_elements = group_app_elements.order_by(model.AppElements.item_id.asc())
        
        total_price = 0
        for app_element in c.group_app_elements:
            if app_element.status == 3:
                pass
            else:
                total_price += app_element.price
        c.total_price = total_price
        
        # Вывод корректных названий групп
        groups_q = meta.Session.query(model.Group)    
        c.available_groups = [(group.uid, group.view) for group in groups_q]

        # Текущий год
        c.year = datetime.datetime.now().strftime('%Y')        

        # Вывод информации о лимитах
        users = request.environ['authkit.users']
        limit_q = meta.Session.query(model.Limit)
        try:
            c.limit = limit_q.filter_by(campaign_id = app_globals.current_campaign_id).filter_by(group_uid = boss_group).first()
        except:
            c.limit = '0'

        return render('/derived/app/group_view_print.html')
        
    
    @authorize(HasAuthKitRole(['boss'])) 
    def delete_item_group(self):
        """Удаление объекта из заявки по отделу"""
        # Удаление элементов из заявки. Они не удаляются полностью, статус меняется на 3
        app_elements_q = meta.Session.query(model.AppElements)
        current_app_element = app_elements_q.filter_by(id = request.urlvars['id']).first()
        if current_app_element.status == 3:
            pass
        else:
            current_app_element.status = 3
        meta.Session.commit()  
        h.redirect(url(controller='app', action='group_app')) 

    @authorize(HasAuthKitRole(['boss'])) 
    def restore_item_group(self):
        """Восстановление объекта в заявке по отделу"""
        # Восстанавливает элемент. Статус меняется на 2.
        app_elements_q = meta.Session.query(model.AppElements)
        current_app_element = app_elements_q.filter_by(id = request.urlvars['id']).first()
        if current_app_element.status == 3:
            current_app_element.status = 2
        meta.Session.commit()  
        h.redirect(url(controller='app', action='group_app')) 
    
    @authorize(HasAuthKitRole(['boss'])) 
    def edit_item_group_form(self):
        """Открывает новое окно для изменения конкретного элемента"""
        user_app_element = meta.Session.query(model.AppElements).filter_by(id = request.urlvars['id'])
        c.user_app_element = user_app_element
        
        finsource_q = meta.Session.query(model.FinSource)
        c.available_finsource = [(finsource.id, finsource.name) for finsource in finsource_q]     
        needs_q = meta.Session.query(model.Needs)
        c.available_needs = [(needs.id, needs.name) for needs in needs_q]
        users = request.environ['authkit.users']
        
        groups_q = meta.Session.query(model.Group)
        c.available_groups = [(group.uid, group.view) for group in groups_q]
        
        # Информациия о заявке           
        values = {}
        element_amount = {}
        element_price = {}
        total_price = 0
        for element in user_app_element:
            values['quarter1'] = element.quarter1
            values['quarter2'] = element.quarter2
            values['quarter3'] = element.quarter3
            values['quarter4'] = element.quarter4
            values['finsource'] = element.finsource
            values['needs'] = element.needs
            values['place'] = element.place
            values['note'] = element.note
            
            element_amount[element.id] = element.quarter1 + element.quarter2 + element.quarter3 + element.quarter4
            element_price[element.id] = element_amount[element.id] * element.items.price
            total_price += element_price[element.id]
        
        c.element_amount = element_amount
        c.element_price = element_price  
        c.total_price = total_price
        return htmlfill.render(render('/derived/app/edit_item_group_form.html'), values)
        #return render('/derived/app/edit_item_group_form.html')
    
    @authorize(HasAuthKitRole(['boss'])) 
    @validate(schema=SaveGroupApp(), form='edit_item_group_form')
    def edit_item_group(self):
        """Изменения элемента заявки по отделу"""
        app_elements_q = meta.Session.query(model.AppElements)
        current_app_element = app_elements_q.filter_by(id = request.urlvars['id']).first()
   
        current_app_element.quarter1 = self.form_result[u'quarter1']
        current_app_element.quarter2 = self.form_result[u'quarter2']
        current_app_element.quarter3 = self.form_result[u'quarter3']
        current_app_element.quarter4 = self.form_result[u'quarter4']
        current_app_element.amount = int(current_app_element.quarter1) + int(current_app_element.quarter2) + int(current_app_element.quarter3) + int(current_app_element.quarter4)
        current_app_element.price = int(current_app_element.amount) * int(current_app_element.items.price)
        current_app_element.finsource = self.form_result[u'finsource']
        current_app_element.needs = self.form_result[u'needs']
        current_app_element.place = self.form_result[u'place']
        current_app_element.note = self.form_result[u'note']
        current_app_element.status = 1
        meta.Session.commit()
        h.redirect(url(controller='app', action='edit_item_group_form', id=request.urlvars['id'])) 
    
    @authorize(HasAuthKitRole(['boss']))     
    def change_item_group_form(self):
        """Форма замены элементы заявки по отделу на другой"""
        h.redirect(url(controller='app', action='group_app')) 

    @authorize(HasAuthKitRole(['boss'])) 
    def change_item_group(self):
        """Замена элементы заявки по отделу на другой"""
        h.redirect(url(controller='app', action='group_app')) 
    
    @authorize(HasAuthKitRole(['boss'])) 
    def app_to_director(self):
        """Передача заявки по отделу ответственному по предприятию на 
           устверждение.
           Сотрудникам, которые заполняли заявки, высылаются письма на e-mail"""
        # Выбор группы
        boss_q = meta.Session.query(model.User)
        boss_group = boss_q.filter_by(username = request.environ['REMOTE_USER']).first().group_uid
        # Выбор пользователей этой группы
        users_q = meta.Session.query(model.User)
        users_in_group = users_q.filter_by(group_uid = boss_group).all()      
        # Выбор заявки и элементов заявки дла этой группы
        for user in users_in_group:       
            app_q = meta.Session.query(model.App)
            current_app = app_q.filter_by(author_id = user.uid).filter_by(campaign_id = app_globals.current_campaign_id) 
            current_app = current_app.filter(or_(model.App.status.like(2), model.App.status.like(3))).first()  
            # Передача заявки ответственному по предприятию
            try:
                current_app.status = 3 
                meta.Session.commit()   
                # Отправить письмо
                mail = user.mail
                fromaddr = 'cniikometa.ru'
                toaddrs = str(mail)
                msg = "Subject: Заявка\nContent-Type: text/plain; charset='UTF-8'\nВаша заявка утверждена ответственным по подразделению."
                server = smtplib.SMTP('localhost')
                server.sendmail(fromaddr, toaddrs, msg)
                server.quit()
            except:
                pass 
        h.redirect(url(controller='app', action='group_app'))
    
    @authorize(HasAuthKitRole(['director'])) 
    def global_app(self):
        """Обобщённая заявка по предприятию"""
        # Пустой запрос
        global_app_elements = meta.Session.query(model.AppElements).filter_by(id = 0)
        
        # Выбор нужных заявок и элементов заявки    
        app_q = meta.Session.query(model.App)
        approved_apps = app_q.filter_by(campaign_id = app_globals.current_campaign_id)
        approved_apps = approved_apps.filter(or_(model.App.status.like(3), model.App.status.like(4))).all()
        for approved_app in approved_apps:
            app_elements_q = meta.Session.query(model.AppElements)
            app_elements = app_elements_q.filter_by(app_id = approved_app.id)
            try:
                global_app_elements = global_app_elements.union(app_elements) 
            except:
                pass     
        c.global_app_elements = global_app_elements.order_by(model.AppElements.item_id.asc())
        
        total_price = 0
        for app_element in c.global_app_elements:
            if app_element.status == 3:
                pass
            else:
                total_price += app_element.price
        c.total_price = total_price
        
        # Корректное отображение названий групп
        groups_q = meta.Session.query(model.Group)    
        c.available_groups = [(group.uid, group.view, group.name) for group in groups_q]
        
        # Сумма по группам
        users = request.environ['authkit.users']
        c.users = users

        total_group_price = {}

        for group in c.users.list_groups():
            # Пустой запрос
            group_app_elements = meta.Session.query(model.AppElements).filter_by(id = 0)
            # Выбор группы
            boss_group = c.users.group_uid(group)
            c.boss_group_view = c.users.group_view(group)
            # Выбор пользователей в этой группе
            users_q = meta.Session.query(model.User)
            users_in_group = users_q.filter_by(group_uid = boss_group).all()
            
            item_q = meta.Session.query(model.Item)
            items = item_q
            
            # Выбор заявки и элементов заявок, соответстующих определённой группе
            for user in users_in_group:       
                app_q = meta.Session.query(model.App)
                current_app = app_q.filter_by(author_id = user.uid).filter_by(campaign_id = app_globals.current_campaign_id) 
                current_app = current_app.filter(or_(model.App.status.like(2), model.App.status.like(3), model.App.status.like(4))).first()  
                app_elements_q = meta.Session.query(model.AppElements)
                try:
                    current_app_elements = app_elements_q.filter_by(app_id = current_app.id)
                    group_app_elements = group_app_elements.union(current_app_elements) 
                except:
                    pass     
            c.group_app_elements = group_app_elements.order_by(model.AppElements.item_id.asc())
            
            total_price = 0
            for app_element in c.group_app_elements:
                if (app_element.status == 3) or (app_element.status == 8):
                    pass
                else:
                    total_price += app_element.price
            total_group_price[group] = total_price

            c.total_group_price = total_group_price
            
        # Вывод информации о лимитах
        limit_q = meta.Session.query(model.Limit)
        try:
            c.limit = limit_q.filter_by(campaign_id = app_globals.current_campaign_id).all()
        except:
            pass
        
        return render('/derived/app/global_view.html')
    
    def global_app_print(self):
        """Обобщённая заявка по предприятию - версия для печати """
        #response.content_type = 'application/download'
        
        # Пустой запрос
        global_app_elements = meta.Session.query(model.AppElements).filter_by(id = 0)
        
        # Выбор нужных заявок и элементов заявки    
        app_q = meta.Session.query(model.App)
        approved_apps = app_q.filter_by(campaign_id = app_globals.current_campaign_id)
        approved_apps = approved_apps.filter(or_(model.App.status.like(3), model.App.status.like(4))).all()
        for approved_app in approved_apps:
            app_elements_q = meta.Session.query(model.AppElements)
            app_elements = app_elements_q.filter_by(app_id = approved_app.id)
            try:
                global_app_elements = global_app_elements.union(app_elements) 
            except:
                pass     
        c.global_app_elements = global_app_elements.order_by(model.AppElements.item_id.asc())
        
        total_price = 0
        for app_element in c.global_app_elements:
            if app_element.status == 3:
                pass
            else:
                total_price += app_element.price
        c.total_price = total_price
        
        # Корректное отображение названий групп
        groups_q = meta.Session.query(model.Group)    
        c.available_groups = [(group.uid, group.view) for group in groups_q]
        
        # Сегодняшняя дата
        c.now = datetime.datetime.now().strftime('%d.%m.%Y') 
    
        # Сумма по группам
        users = request.environ['authkit.users']
        c.users = users

        total_group_price = {}

        for group in c.users.list_groups():
            # Пустой запрос
            group_app_elements = meta.Session.query(model.AppElements).filter_by(id = 0)
            # Выбор группы
            boss_group = c.users.group_uid(group)
            c.boss_group_view = c.users.group_view(group)
            # Выбор пользователей в этой группе
            users_q = meta.Session.query(model.User)
            users_in_group = users_q.filter_by(group_uid = boss_group).all()
            
            # Выбор заявки и элементов заявок, соответстующих определённой группе
            for user in users_in_group:       
                app_q = meta.Session.query(model.App)
                current_app = app_q.filter_by(author_id = user.uid).filter_by(campaign_id = app_globals.current_campaign_id) 
                current_app = current_app.filter(or_(model.App.status.like(2), model.App.status.like(3))).first()  
                app_elements_q = meta.Session.query(model.AppElements)
                try:
                    current_app_elements = app_elements_q.filter_by(app_id = current_app.id)
                    group_app_elements = group_app_elements.union(current_app_elements) 
                except:
                    pass     
            c.group_app_elements = group_app_elements.order_by(model.AppElements.item_id.asc())
            
            total_price = 0
            for app_element in c.group_app_elements:
                if (app_element.status == 3) or (app_element.status == 8):
                    pass
                else:
                    total_price += app_element.price
            total_group_price[group] = total_price

            c.total_group_price = total_group_price
            
        # Вывод информации о лимитах
        limit_q = meta.Session.query(model.Limit)
        try:
            c.limit = limit_q.filter_by(campaign_id = app_globals.current_campaign_id).all()
        except:
            pass
        
        return render('/derived/app/global_view_print.html')
        
    @authorize(HasAuthKitRole(['director'])) 
    def approve_global_app(self):
        """Утверждение заявки по предприятию"""
        # Выбор нужных  заявок и элементов заявок
        app_q = meta.Session.query(model.App)
        approved_apps = app_q.filter_by(campaign_id = app_globals.current_campaign_id).filter_by(status = 3).all()
        for approved_app in approved_apps:
            # Утверждение заявки
            try:
                approved_app.status = 4
                meta.Session.commit()   
                
                # Выбрать автора заявки
                users_q = meta.Session.query(model.User)
                user = users_q.filter_by(id = approved_app.author_id).first()  
                # Отправить письмо
                mail = user.mail
                fromaddr = 'cniikometa.ru'
                toaddrs = str(mail)
                msg = "Subject: Заявка\nContent-Type: text/plain; charset='UTF-8'\nВаша заявка утверждена ответственным по предприятию."
                server = smtplib.SMTP('localhost')
                server.sendmail(fromaddr, toaddrs, msg)
                server.quit()
            except:
                pass         
        h.redirect(url(controller='app', action='global_app'))
    
    @authorize(HasAuthKitRole(['director'])) 
    def sale_app(self): 
        """Вывод формы для реализации заявок"""
        # Пустой запрос
        global_app_elements = meta.Session.query(model.AppElements).filter_by(id = 0)
        values = {}
        
        # Выбор нужных заявок и элементов заявки  
        app_q = meta.Session.query(model.App)
        approved_apps = app_q.filter_by(campaign_id = app_globals.current_campaign_id)
        approved_apps = approved_apps.filter(or_(model.App.status.like(4), model.App.status.like(4))).all()
        for approved_app in approved_apps:
            app_elements_q = meta.Session.query(model.AppElements)
            app_elements = app_elements_q.filter_by(app_id = approved_app.id)
            for element in app_elements:
                values['quarter1_el'+str(element.id)] = element.quarter1
                values['quarter2_el'+str(element.id)] = element.quarter2
                values['quarter3_el'+str(element.id)] = element.quarter3
                values['quarter4_el'+str(element.id)] = element.quarter4
                values['quarter1p_el'+str(element.id)] = element.quarter1p
                values['quarter2p_el'+str(element.id)] = element.quarter2p
                values['quarter3p_el'+str(element.id)] = element.quarter3p
                values['quarter4p_el'+str(element.id)] = element.quarter4p
                values['finsource_el'+str(element.id)] = element.finsource
                values['needs_el'+str(element.id)] = element.needs
                values['place_el'+str(element.id)] = element.place
                values['note_el'+str(element.id)] = element.note    
                values['action_el'+str(element.id)] = element.status         
            try:               
                global_app_elements = global_app_elements.union(app_elements) 
            except:
                pass     
        c.global_app_elements = global_app_elements.order_by(model.AppElements.item_id.asc())
        
        total_price = 0
        total_pricep = 0
        for app_element in c.global_app_elements:
            if (app_element.status == 3) or (app_element.status == 8):
                pass
            else:
                total_price += app_element.price
                total_pricep += app_element.pricep
        c.total_price = total_price
        c.total_pricep = total_pricep
        
        # Действия
        c.available_actions = [
                                  (5, u'Закуплено'),
                                  (6, u'Изменено'),
                                  (7, u'Заменено'),
                                  (8, u'Не закуплено'),
                              ]
        
        # Корректное отображение названий групп
        groups_q = meta.Session.query(model.Group)    
        c.available_groups = [(group.uid, group.view) for group in groups_q]
        #return render('/derived/app/sale_view.html')
        return htmlfill.render(render('/derived/app/sale_view.html'), values)
    
    @authorize(HasAuthKitRole(['director'])) 
    def sale_app_print(self): 
        """Формы реализации заявки - версия для печати """
        #response.content_type = 'application/download'
        # Пустой запрос
        global_app_elements = meta.Session.query(model.AppElements).filter_by(id = 0)
        values = {}
        
        # Выбор нужных заявок и элементов заявки  
        app_q = meta.Session.query(model.App)
        approved_apps = app_q.filter_by(campaign_id = app_globals.current_campaign_id)
        approved_apps = approved_apps.filter(or_(model.App.status.like(4), model.App.status.like(4))).all()
        for approved_app in approved_apps:
            app_elements_q = meta.Session.query(model.AppElements)
            app_elements = app_elements_q.filter_by(app_id = approved_app.id)
            for element in app_elements:
                values['quarter1_el'+str(element.id)] = element.quarter1
                values['quarter2_el'+str(element.id)] = element.quarter2
                values['quarter3_el'+str(element.id)] = element.quarter3
                values['quarter4_el'+str(element.id)] = element.quarter4
                values['quarter1p_el'+str(element.id)] = element.quarter1p
                values['quarter2p_el'+str(element.id)] = element.quarter2p
                values['quarter3p_el'+str(element.id)] = element.quarter3p
                values['quarter4p_el'+str(element.id)] = element.quarter4p
                values['finsource_el'+str(element.id)] = element.finsource
                values['needs_el'+str(element.id)] = element.needs
                values['place_el'+str(element.id)] = element.place
                values['note_el'+str(element.id)] = element.note    
                values['action_el'+str(element.id)] = element.status         
            try:               
                global_app_elements = global_app_elements.union(app_elements) 
            except:
                pass     
        c.global_app_elements = global_app_elements.order_by(model.AppElements.item_id.asc())
        
        total_price = 0
        total_pricep = 0
        for app_element in c.global_app_elements:
            if app_element.status == 3:
                pass
            else:
                total_price += app_element.price
                total_pricep += app_element.pricep
        c.total_price = total_price
        c.total_pricep = total_pricep
        
        # Корректное отображение названий групп
        groups_q = meta.Session.query(model.Group)    
        c.available_groups = [(group.uid, group.view) for group in groups_q]
        
        # Текущий год
        c.year = datetime.datetime.now().strftime('%Y')
        
        return htmlfill.render(render('/derived/app/sale_view_print.html'), values)    
    
    @authorize(HasAuthKitRole(['director'])) 
    @validate(schema=SaveApp(), form='sale_app')   
    def save_sale_app(self):
        """Реализация заявок"""
        # Выбор нужных заявок и элементов заявок  
        app_q = meta.Session.query(model.App)
        approved_apps = app_q.filter_by(campaign_id = app_globals.current_campaign_id)
        approved_apps = approved_apps.filter(or_(model.App.status.like(4), model.App.status.like(4))).all()
        for approved_app in approved_apps:
            app_elements_q = meta.Session.query(model.AppElements)
            app_elements = app_elements_q.filter_by(app_id = approved_app.id)
        
            for element in app_elements:
                element.quarter1p = self.form_result[u'quarter1p_el'+str(element.id)]
                element.quarter2p = self.form_result[u'quarter2p_el'+str(element.id)]
                element.quarter3p = self.form_result[u'quarter3p_el'+str(element.id)]
                element.quarter4p = self.form_result[u'quarter4p_el'+str(element.id)]
                element.amountp = int(element.quarter1p) + int(element.quarter2p) + int(element.quarter3p) + int(element.quarter4p)
                element.price = int(element.amount) * int(element.items.price)
                element.pricep = int(element.amountp) * int(element.items.price)
                element.status = self.form_result[u'action_el'+str(element.id)]
                meta.Session.commit()
        
        h.redirect(url(controller='app', action='sale_app'))
        
    def mail_sale_app(self):
        """Информирование сотрудников по e-mail о результатах реализации"""
        # Выбор пользователей
        users_q = meta.Session.query(model.User)
        users = users_q.all()      
        for user in users:         
            try:
                # Отправить письмо
                mail = user.mail
                fromaddr = 'cniikometa.ru'
                toaddrs = str(mail)
                msg = "Subject: Заявка\nContent-Type: text/plain; charset='UTF-8'\nВаша заявка реализована."
                server = smtplib.SMTP('localhost')
                server.sendmail(fromaddr, toaddrs, msg)
                server.quit()
            except:
                pass
        h.redirect(url(controller='app', action='sale_app'))
    
    def director_app_to_global(self):
        """Ответственный по предприятию добавляет свою заявку к общей"""
        app_q = meta.Session.query(model.App)
        current_app = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first() 
        if current_app.status == 1:
            current_app.status = 4 # Forwarding app to boss
        meta.Session.commit()
        h.redirect(url(controller='app', action='user_app'))