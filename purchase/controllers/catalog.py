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
from pylons.decorators import validate
from pylons.decorators.rest import restrict
from sqlalchemy import delete
import datetime

from pylons import app_globals

log = logging.getLogger(__name__)

class UniqueSection(formencode.validators.FancyValidator):
    """Проверка, уникально ли название раздела"""
    def _to_python(self, values, state):
        section_q = meta.Session.query(model.Section)
        query = section_q.filter_by(name=values['name'])
        if request.urlvars['action'] == 'create_section':
            existing = query.first()
            if existing is not None:
                raise formencode.Invalid("Раздел с таким названием уже "
                    "сущетвует.", values, state)
        return values

class NewSectionForm(formencode.Schema):
    """Проверка данных формы создания нового раздела"""
    allow_extra_fields = True
    filter_extra_fields = True
    name = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':u'Введите название раздела.'
        }
    )
    parent_section = formencode.validators.String(not_empty=True)
    description = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':u'Введите описание раздела.'
        }
    )
    chained_validators = [UniqueSection()]
    
class EditSectionForm(formencode.Schema):
    """Проверка данных формы изменения нового раздела"""
    allow_extra_fields = True
    filter_extra_fields = True
    name = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':u'Введите название раздела.'
        }
    )
    description = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':u'Введите описание раздела.'
        }
    )
    chained_validators = [UniqueSection()]
    
class DeleteSectionForm(formencode.Schema):
    """Проверка данных формы удаления нового раздела"""
    allow_extra_fields = True
    filter_extra_fields = True
    parent_section = formencode.validators.String(not_empty=True)
    
class NewItemForm(formencode.Schema):
    """Проверка данных формы создания нового объекта"""
    allow_extra_fields = True
    filter_extra_fields = True
    brand = formencode.validators.String(not_empty=True)
    model = formencode.validators.String(not_empty=True)
    description = formencode.validators.String(not_empty=True)
    section_id = formencode.validators.String(not_empty=True)
    unit_id = formencode.validators.Int(not_empty=True)
    price = formencode.validators.Number(not_empty=True)
    
class SearchForm(formencode.Schema):
    """Проверка данных формы поиска"""
    allow_extra_fields = True
    filter_extra_fields = True
    search_string = formencode.validators.String(not_empty=True)

class CatalogController(BaseController):
    
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

    def index(self):
        """Отображает список основных разделов (первый уровень)"""
        section_q = meta.Session.query(model.Section)
        c.section = section_q
        c.main_sections = section_q.filter_by(parent_section_id = 1)
        h.redirect(url(controller='catalog', action='section', id=1))
    
    def section(self, id):        
        """Отображает список подразделов и breadcrumbs"""
        section_q = meta.Session.query(model.Section)
        c.section = section_q
             
        def breadcrumbs(section_id):
            "Отображает список разделов до Главного"
            a = ''
            b = []
            d = []
            while a != None:
                a = c.section.filter_by(id = section_id).first().parent_section_id
                a_name = c.section.filter_by(id = section_id).first().name
                a_id = c.section.filter_by(id = section_id).first().id
                if a != None:
                    b = [(a_name, a_id)] + b
                section_id = a
            c.breadcrumbs = b
        
        #try:
        c.current_section = section_q.filter_by(id = id).first()
        breadcrumbs(c.current_section.id)
        
        # item_q = meta.Session.query(model.Item)
        # c.section_items = item_q.filter_by(section_id = c.current_section.id)
        # Just using ORM relation instead of another query
        c.section_items = c.current_section.items
            
        # To disable "Add" link
        app_q = meta.Session.query(model.App)
        c.current_app_status = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first().status
        
        app_globals.current_section_id = c.current_section.id
        return render('/derived/catalog/section.html')
        #except:
            #h.redirect(url(controller='catalog', action='section', id='1'))
    
    def new_section(self):
        """Отображение формы для создания раздела"""
        section_q = meta.Session.query(model.Section)
        c.available_sections = [(section.id, section.name) for section in section_q]
        return render('/derived/catalog/new_section.html')
    
    @validate(schema=NewSectionForm(), form='new_section')
    def create_section(self):
        """Создание раздела"""
        section = model.Section()
        section.name = self.form_result['name']
        section.parent_section_id = self.form_result['parent_section']
        section.description = self.form_result['description']
        meta.Session.add(section)
        meta.Session.flush()
        h.redirect(url(controller='catalog', action='section', id=section.id))
        
    def edit_section(self):
        """Отображение формы для изменения/удаления раздела"""
        section_q = meta.Session.query(model.Section)
        section = section_q.filter_by(id=request.urlvars['id']).first()
        c.current_section = section
        c.available_sections = [(section.id, section.name) for section in section_q]
        values = {
            'name': c.current_section.name,
            'parent_section': c.current_section.id,
            'description': c.current_section.description
        }
        return htmlfill.render(render('/derived/catalog/edit_section.html'), values)
    
    @validate(schema=EditSectionForm(), form='edit_section')
    def save_section(self):
        """Сохранения параметров раздела"""
        section_q = meta.Session.query(model.Section)
        section = section_q.filter_by(id=request.urlvars['id']).first()
        section.name = self.form_result['name']
        section.description = self.form_result['description']
        section.edited = datetime.datetime.now()
        meta.Session.commit()
        h.redirect(url(controller='catalog', action='section', id=section.id))
    
    @validate(schema=DeleteSectionForm(), form='delete')
    def delete_section(self):
        """Удаляет раздел и все дочерние разделы"""
        section_q = meta.Session.query(model.Section)
        section = section_q.filter_by(id=request.urlvars['id']).first()
        meta.Session.delete(section)
        meta.Session.commit()
        h.redirect(url(controller='catalog', action='section', id=section.parent_section_id))
    
    def new_item(self):
        """Отображение формы для создания объекта"""
        section_q = meta.Session.query(model.Section)
        available_sections = [(section.id, section.name) for section in section_q]
        c.available_sections = available_sections[1:]
        unit_q = meta.Session.query(model.Unit)
        c.available_units = [(unit.id, unit.name) for unit in unit_q]
        return render('/derived/catalog/new_item.html')
    
    @validate(schema=NewItemForm(), form='new_item')
    def create_item(self):
        """Создание объекта"""
        item = model.Item()
        item.brand = self.form_result['brand']
        item.model = self.form_result['model']
        item.description = self.form_result['description']
        item.section_id = self.form_result['section_id']
        item.unit_id = self.form_result['unit_id']
        item.price = self.form_result['price']
        meta.Session.add(item)
        meta.Session.flush()
        h.redirect(url(controller='catalog', action='new_item'))
    
    def edit_item(self):
        """Отображение формы для изменения/удаления объекта"""
        section_q = meta.Session.query(model.Section)
        c.available_sections = [(section.id, section.name) for section in section_q]
        unit_q = meta.Session.query(model.Unit)
        c.available_units = [(unit.id, unit.name) for unit in unit_q]
        item_q = meta.Session.query(model.Item)
        item = item_q.filter_by(id=request.urlvars['id']).first()
        c.current_item = item
        values = {
            'brand': c.current_item.brand,
            'model': c.current_item.model,
            'description': c.current_item.description,
            'section_id': c.current_item.section_id,
            'unit_id': c.current_item.unit_id,
            'price': c.current_item.price,
        }
        #return render('/derived/catalog/edit.html')
        return htmlfill.render(render('/derived/catalog/edit_item.html'), values)
    
    @validate(schema=NewItemForm(), form='edit_item')
    def save_item(self, id):
        """Сохранение параметров объекта"""
        item_q = meta.Session.query(model.Item)
        item = item_q.filter_by(id=id).first()
        item.brand = self.form_result['brand']
        item.model = self.form_result['model']
        item.description = self.form_result['description']
        item.section_id = self.form_result['section_id']
        item.unit_id = self.form_result['unit_id']
        item.price = self.form_result['price']
        item.edited = datetime.datetime.now()
        meta.Session.commit()
        h.redirect(url(controller='catalog', action='section', id=item.section_id))
    
    def delete_item(self):
        """Удаление объекта"""
        item_q = meta.Session.query(model.Item)
        item = item_q.filter_by(id=request.urlvars['id']).first()
        # Объект не удаляется из базы данных, а просто становится невидимым
        # Это необходимо, чтобы сохранилась информация в старых заявках
        item.deleted = 1
        #meta.Session.delete(item)
        meta.Session.commit()
        h.redirect(url(controller='catalog', action='section', id=item.section_id))
    
    @validate(schema=SearchForm(), form='section')    
    def search_item(self):
        """Поиск объектов по каталогу"""
        section_q = meta.Session.query(model.Section)
        c.section = section_q
        
        item_q = meta.Session.query(model.Item)
        c.search_results = item_q.filter_by(brand=self.form_result['search_string']).all()
        
        # To disable "Add" link
        app_q = meta.Session.query(model.App)
        c.current_app_status = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first().status
        
        return render('/derived/catalog/search_item.html')