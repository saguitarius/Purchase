## -*- coding: utf-8 -*-

import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from purchase.lib.base import BaseController, render

import purchase.model as model
import purchase.model.meta as meta
import purchase.lib.helpers as h

import formencode
from formencode import htmlfill
from pylons.decorators import validate
from pylons.decorators.rest import restrict
from sqlalchemy import delete
import datetime

log = logging.getLogger(__name__)

class NewSectionForm(formencode.Schema):
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
    
class DeleteSectionForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    parent_section = formencode.validators.String(not_empty=True)

class CatalogController(BaseController):

    def index(self):
        "Returns list of main sections (inherited from Home)"
        section_q = meta.Session.query(model.Section)
        c.section = section_q
        return render('/derived/catalog/catalog.html')
    
    def section(self):        
        "Returns list of subsections and breadcrumbs"
        section_q = meta.Session.query(model.Section)
        c.section = section_q
             
        def breadcrumbs(item_id):
            "Returns list of sectins up to Home"
            a = ''
            b = []
            while a != None:
                a = c.section.filter_by(id = item_id).first().parent_section_id
                a_name = c.section.filter_by(id = item_id).first().name
                if a != None:
                    b = [a_name] + b
                item_id = a
            return b    
        
        #try:
        request.params['name']
        current_section = request.params['name']
        c.current_section = section_q.filter_by(name = current_section).first()
        c.breadcrumbs = breadcrumbs(c.current_section.id)
        return render('/derived/catalog/section.html')
        #except:
            #h.redirect(url(controller='catalog', action='index'))
            
    def new_section(self):
        "Renders form for creating a section"
        section_q = meta.Session.query(model.Section)
        c.available_sections = [(section.id, section.name) for section in section_q]
        return render('/derived/catalog/new_section.html')
    
    @validate(schema=NewSectionForm(), form='new')
    def create_section(self):
        "Creates section"
        section = model.Section()
        section.name = self.form_result['name']
        section.parent_section_id = self.form_result['parent_section']
        section.description = self.form_result['description']
        meta.Session.add(section)
        meta.Session.flush()
        h.redirect(url(controller='catalog', action='section', name=section.name))
        
    def edit_section(self):
        "Renders form for editing/deleting a section"
        section_q = meta.Session.query(model.Section)
        section = section_q.filter_by(name=request.params['name']).first()
        c.current_section = section
        c.available_sections = [(section.id, section.name) for section in section_q]
        values = {
            'name': c.current_section.name,
            'parent_section': c.current_section.id,
            'description': c.current_section.description
        }
        #return render('/derived/catalog/edit.html')
        return htmlfill.render(render('/derived/catalog/edit_section.html'), values)
    
    @validate(schema=NewSectionForm(), form='new')
    def save_section(self):
        "Saves changes"
        section_q = meta.Session.query(model.Section)
        section = section_q.filter_by(id=self.form_result['parent_section']).first()
        section.name = self.form_result['name']
        section.description = self.form_result['description']
        section.edited = datetime.datetime.now()
        meta.Session.commit()
        h.redirect(url(controller='catalog', action='section', name=section.name))
    
    @validate(schema=DeleteSectionForm(), form='delete')
    def delete_section(self):
        "Deletes section and all child sections"
        section_q = meta.Session.query(model.Section)
        section = section_q.filter_by(name=request.params['name']).first()
        meta.Session.delete(section)
        meta.Session.commit()
        h.redirect(url(controller='catalog', action='index'))