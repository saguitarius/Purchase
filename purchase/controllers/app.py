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

log = logging.getLogger(__name__)

class App_Element(formencode.Schema):
    quarter1 = formencode.validators.Int(not_empty=True)
    quarter2 = formencode.validators.Int(not_empty=True)
    quarter3 = formencode.validators.Int(not_empty=True)
    quarter4 = formencode.validators.Int(not_empty=True)
    finsource = formencode.validators.String(not_empty=True)
    needs = formencode.validators.String(not_empty=True)
    place = formencode.validators.String(not_empty=True)
    
class SaveApp(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = False
    app_element = ForEach(App_Element)
    
class SaveGroupApp(formencode.Schema):
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
    
    @authorize(ValidAuthKitUser())
    def __before__(self):
        '''
            TEMP!!!
        '''
        # Identify user uid and put it into global var
        user_q = meta.Session.query(model.User)
        user = user_q.filter_by(username = request.environ['REMOTE_USER']).first()
        app_globals.user_id = user.uid
        app_globals.user_group = user.group.view
        app_globals.user_view = user.view
            
        campaign_q = meta.Session.query(model.Campaign)
        c.current_campaign = campaign_q.filter_by(status = '1').first()
        # Check if there is an active campaign
        if c.current_campaign:
            app_globals.current_campaign_id = c.current_campaign.id
            app_globals.current_campaign_start_date = c.current_campaign.start_date
            app_globals.current_campaign_end_date = c.current_campaign.end_date        
        '''
            TEMP!!!
        '''
        pass

    """
    App status:
        1 Newly created, can be edited by author
        2 Send to boss for examination, can NOT be edited by author
        3 Examined and forwarded to director, can NOT be edited by author
        4 Approved by director
    """
    
    """
    App Element status:
        0 Pure
        --consolidation-
        1 Options are changed by boss
        2 Item is changed by boss
        3 Deleted by boss
        4 Approved by director
        --realisation--
        5 Purchased
        6 Purchased, other options
        7 Purchased, other item
        8 Not purchased
    """
    
    @authorize(ValidAuthKitUser())
    def user_app(self):
        # Selecting correct app and app elements for particular user
        app_q = meta.Session.query(model.App)
        c.current_app = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first()   
        app_elements_q = meta.Session.query(model.AppElements)
        c.current_app_elements = app_elements_q.filter_by(app_id = c.current_app.id)
        
        # All available selections
        finsource_q = meta.Session.query(model.FinSource)
        c.available_finsource = [(finsource.id, finsource.name) for finsource in finsource_q]     
        needs_q = meta.Session.query(model.Needs)
        c.available_needs = [(needs.id, needs.name) for needs in needs_q]
        users = request.environ['authkit.users']
        
        # c.available_groups = users.list_groups()  
        groups_q = meta.Session.query(model.Group)    
        c.available_groups = [(group.uid, group.view) for group in groups_q]
        
        # Stored app info            
        values = {}
        element_amount = {}
        element_price = {}
        total_price = 0
        for element in c.current_app_elements:
            values['quarter1_el'+str(element.id)] = element.quarter1
            values['quarter2_el'+str(element.id)] = element.quarter2
            values['quarter3_el'+str(element.id)] = element.quarter3
            values['quarter4_el'+str(element.id)] = element.quarter4
            values['finsource_el'+str(element.id)] = element.finsource
            values['needs_el'+str(element.id)] = element.needs
            values['place_el'+str(element.id)] = element.place
            values['note_el'+str(element.id)] = element.note
            
            element_amount[element.id] = element.quarter1 + element.quarter2 + element.quarter3 + element.quarter4
            element_price[element.id] = element_amount[element.id] * element.items.price
            if element.status == 3:
                pass
            else:
                total_price += element_price[element.id]
        
        c.element_amount = element_amount
        c.element_price = element_price  
        c.total_price = total_price
        
        c.all_apps = app_q.filter_by(author_id = app_globals.user_id).all()
        
        return htmlfill.render(render('/derived/app/user_view.html'), values)
    
    @authorize(ValidAuthKitUser())
    def add_item(self):
        app_q = meta.Session.query(model.App)
        c.current_app = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first()
        if (c.current_app.status == 1) or (h.auth.authorized(h.auth.is_valid_user)):    
            app_elements_q = meta.Session.query(model.AppElements)
            # Check if this element is already in the app
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
                app_elements.amount = '0'
                app_elements.price = '0'
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
        app_elements_q = meta.Session.query(model.AppElements)
        app_element = app_elements_q.filter_by(id = request.urlvars['id']).first()
        meta.Session.delete(app_element)
        meta.Session.commit()
        h.redirect(url(controller='app', action='user_app'))
    
    @authorize(ValidAuthKitUser())
    @validate(schema=SaveApp(), form='user_app')    
    def save_user_app(self):
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
        # User sends app to boss
        app_q = meta.Session.query(model.App)
        current_app = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first() 
        if current_app.status == 1:
            current_app.status = 2 # Forwarding app to boss
        meta.Session.commit()
        h.redirect(url(controller='app', action='user_app'))
    
    @authorize(HasAuthKitRole(['boss']))    
    def group_app(self): 
        # Empty query
        group_app_elements = meta.Session.query(model.AppElements).filter_by(id = 0)
        # Selecting group
        boss_q = meta.Session.query(model.User)
        boss_group = boss_q.filter_by(username = request.environ['REMOTE_USER']).first().group_uid
        c.boss_group_view = boss_q.filter_by(username = request.environ['REMOTE_USER']).first().group.view
        # Selecting users in this group
        users_q = meta.Session.query(model.User)
        users_in_group = users_q.filter_by(group_uid = boss_group).all()
        
        # Selecting correct app and app elements for particular group
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
        
        # To name groups correctly
        groups_q = meta.Session.query(model.Group)    
        c.available_groups = [(group.uid, group.view) for group in groups_q]
        
####################################
###        # Big table with fileds. No use.
###        # All available selections
###        finsource_q = meta.Session.query(model.FinSource)
###        c.available_finsource = [(finsource.id, finsource.name) for finsource in finsource_q]     
###        needs_q = meta.Session.query(model.Needs)
###        c.available_needs = [(needs.id, needs.name) for needs in needs_q]
###        users = request.environ['authkit.users']
###        
###        groups_q = meta.Session.query(model.Group)
###        c.available_groups = [(group.uid, group.view) for group in groups_q]
###        
###        # Stored app info            
###        values = {}
###        element__amount = {}
###        element__price = {}
###        total__price = 0
###        for element in c.group_app_elements:
###            values['quarter1_el'+str(element.id)] = element.quarter1
###            values['quarter2_el'+str(element.id)] = element.quarter2
###            values['quarter3_el'+str(element.id)] = element.quarter3
###            values['quarter4_el'+str(element.id)] = element.quarter4
###            values['finsource_el'+str(element.id)] = element.finsource
###            values['needs_el'+str(element.id)] = element.needs
###            values['place_el'+str(element.id)] = element.place
###            values['note_el'+str(element.id)] = element.note
###            
###            element__amount[element.id] = element.quarter1 + element.quarter2 + element.quarter3 + element.quarter4
###            element__price[element.id] = element__amount[element.id] * element.items.price
###            total__price += element__price[element.id]
###        
###        c.element__amount = element__amount
###        c.element__price = element__price  
###        c.total__price = total__price
###        return htmlfill.render(render('/derived/app/group_view.html'), values)
####################################
        
        # Total price etc.
        return render('/derived/app/group_view.html')
        
    
    @authorize(HasAuthKitRole(['boss'])) 
    def delete_item_group(self):
        # Deletes element from app. It's still there, but status = 3
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
        # Restores element. Status becomes 2.
        app_elements_q = meta.Session.query(model.AppElements)
        current_app_element = app_elements_q.filter_by(id = request.urlvars['id']).first()
        if current_app_element.status == 3:
            current_app_element.status = 2
        meta.Session.commit()  
        h.redirect(url(controller='app', action='group_app')) 
    
    @authorize(HasAuthKitRole(['boss'])) 
    def edit_item_group_form(self):
        # Opens new window for editing particulam app element
        user_app_element = meta.Session.query(model.AppElements).filter_by(id = request.urlvars['id'])
        c.user_app_element = user_app_element
        
        finsource_q = meta.Session.query(model.FinSource)
        c.available_finsource = [(finsource.id, finsource.name) for finsource in finsource_q]     
        needs_q = meta.Session.query(model.Needs)
        c.available_needs = [(needs.id, needs.name) for needs in needs_q]
        users = request.environ['authkit.users']
        
        groups_q = meta.Session.query(model.Group)
        c.available_groups = [(group.uid, group.view) for group in groups_q]
        
        # Stored app info            
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
        #h.redirect(url(controller='app', action='group_app')) 
        pass

    @authorize(HasAuthKitRole(['boss'])) 
    def change_item_group(self):
        #h.redirect(url(controller='app', action='group_app')) 
        pass
    
    @authorize(HasAuthKitRole(['boss'])) 
    def app_to_director(self):
        # Forward apps to director ~consolidation
        # Selecting group
        boss_q = meta.Session.query(model.User)
        boss_group = boss_q.filter_by(username = request.environ['REMOTE_USER']).first().group_uid
        # Selecting users in this group
        users_q = meta.Session.query(model.User)
        users_in_group = users_q.filter_by(group_uid = boss_group).all()      
        # Selecting correct app and app elements for particular group
        for user in users_in_group:       
            app_q = meta.Session.query(model.App)
            current_app = app_q.filter_by(author_id = user.uid).filter_by(campaign_id = app_globals.current_campaign_id) 
            current_app = current_app.filter(or_(model.App.status.like(2), model.App.status.like(3))).first()  
            # Forwarding app to director
            try:
                current_app.status = 3 
                meta.Session.commit()   
            except:
                pass 
        h.redirect(url(controller='app', action='group_app'))
    
    @authorize(HasAuthKitRole(['director'])) 
    def global_app(self):
        # Global app for the whole enterprise
        # Empty query
        global_app_elements = meta.Session.query(model.AppElements).filter_by(id = 0)
        
        # Selecting correct app and app elements     
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
        
        # To name groups correctly
        groups_q = meta.Session.query(model.Group)    
        c.available_groups = [(group.uid, group.view) for group in groups_q]
        return render('/derived/app/global_view.html')
        
    @authorize(HasAuthKitRole(['director'])) 
    def approve_global_app(self):
        # Selecting correct app and app elements     
        app_q = meta.Session.query(model.App)
        approved_apps = app_q.filter_by(campaign_id = app_globals.current_campaign_id).filter_by(status = 3).all()
        for approved_app in approved_apps:
            # Approving global app
            try:
                approved_app.status = 4
                meta.Session.commit()   
            except:
                pass         
        return render('/derived/app/global_view.html')
    
    @authorize(HasAuthKitRole(['director'])) 
    def sale_app(self): 
        # Realisation of global app  
        # Empty query
        global_app_elements = meta.Session.query(model.AppElements).filter_by(id = 0)
        values = {}
        
        # Selecting correct app and app elements     
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
        for app_element in c.global_app_elements:
            if app_element.status == 3:
                pass
            else:
                total_price += app_element.price
        c.total_price = total_price
        
        # Actions
        c.available_actions = [
                                  (5, u'Закуплено'),
                                  (6, u'Изменено'),
                                  (7, u'Заменено'),
                                  (8, u'Не закуплено'),
                              ]
        
        # To name groups correctly
        groups_q = meta.Session.query(model.Group)    
        c.available_groups = [(group.uid, group.view) for group in groups_q]
        #return render('/derived/app/sale_view.html')
        return htmlfill.render(render('/derived/app/sale_view.html'), values)
    
    @authorize(HasAuthKitRole(['director'])) 
    @validate(schema=SaveApp(), form='sale_app')   
    def save_sale_app(self):
        # Selecting correct app and app elements     
        app_q = meta.Session.query(model.App)
        approved_apps = app_q.filter_by(campaign_id = app_globals.current_campaign_id)
        approved_apps = approved_apps.filter(or_(model.App.status.like(4), model.App.status.like(4))).all()
        for approved_app in approved_apps:
            app_elements_q = meta.Session.query(model.AppElements)
            app_elements = app_elements_q.filter_by(app_id = approved_app.id)
        
            for element in app_elements:
                element.quarter1 = self.form_result[u'quarter1_el'+str(element.id)]
                element.quarter2 = self.form_result[u'quarter2_el'+str(element.id)]
                element.quarter3 = self.form_result[u'quarter3_el'+str(element.id)]
                element.quarter4 = self.form_result[u'quarter4_el'+str(element.id)]
                element.amount = int(element.quarter1) + int(element.quarter2) + int(element.quarter3) + int(element.quarter4)
                element.price = int(element.amount) * int(element.items.price)
                element.status = self.form_result[u'action_el'+str(element.id)]
                meta.Session.commit()
        
        h.redirect(url(controller='app', action='sale_app'))
        
    def director_app_to_global(self):
        # Director adds his own app to the global app directly
        app_q = meta.Session.query(model.App)
        current_app = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first() 
        if current_app.status == 1:
            current_app.status = 4 # Forwarding app to boss
        meta.Session.commit()
        h.redirect(url(controller='app', action='user_app'))