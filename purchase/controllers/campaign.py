## -*- coding: utf-8 -*-

import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons import app_globals

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
import datetime

log = logging.getLogger(__name__)

class Limit(formencode.Schema):
    """Проверка данных форма создания новой кампании"""
    allow_extra_fields = True
    filter_extra_fields = False   
    limit = formencode.validators.Int(not_empty=True)  

class NewCampaignForm(formencode.Schema):
    """Проверка данных форма создания новой кампании"""
    allow_extra_fields = True
    filter_extra_fields = False
    start_date = formencode.validators.DateConverter(not_empty=True, month_style='dd/mm/yyyy')
    #start_date = formencode.validators.DateValidator(after_now=True)
    end_date = formencode.validators.DateConverter(not_empty=True, month_style='dd/mm/yyyy')
    #end_date = formencode.validators.DateValidator(after_now=True)
    description = formencode.validators.String(not_empty=True)
    limits = app_element = ForEach(Limit)

class CampaignController(BaseController):
    
    """Статусы кампаний:
        1 Текущая, запущена, активна
        2 Текущая, окончена, активна
        3 Окончена, не активна
        
        Запущена - пользователи могут создавать заявки
        Окончена - не могут
        
        Активна - ответственный по предприятию может работать с кампанией
        Не активна - не может
    """

    def index(self):
        """Отображение главной страницы"""
        campaign_q = meta.Session.query(model.Campaign)
        c.current_campaign = campaign_q.filter_by(status = '1').first()
        c.finished_active_campaign = campaign_q.filter_by(status = '2').first()
        c.finished_inactive_campaign = campaign_q.filter_by(status = '3').order_by(model.Campaign.id.desc()).all()
        return render('/derived/campaign/view.html')
    
    def new(self):
        """Форма создания новой заявочной кампании"""
        users = request.environ['authkit.users']
        c.users = users
        return render('/derived/campaign/new.html')
    
    @validate(schema=NewCampaignForm(), form='new')
    # Необходимо доделать валидатор
    def create(self):
        """Создание новой заявочной кампании"""
        campaign = model.Campaign()
        campaign.start_date = self.form_result['start_date']
        campaign.end_date = self.form_result['end_date']
        campaign.status = '1'
        campaign.description = self.form_result['description']
        meta.Session.add(campaign)
        meta.Session.flush()
        
        # Установка лимитов по подразделениям
        users = request.environ['authkit.users']
        c.users = users
        for group in users.list_groups():
            limit = model.Limit()
            limit.campaign_id = campaign.id
            limit.group_uid = users.group_uid(group)
            try:
                limit.limit_value = self.form_result['limit'+str(users.group_uid(group))]
            except:
                pass
            meta.Session.add(limit)
            meta.Session.flush()
        
        h.redirect(url(controller='campaign', action='assign_globals'))
        
    def stop(self):
        """Остановка кампании - окончена, активна"""
        campaign_q = meta.Session.query(model.Campaign)
        c.current_campaign = campaign_q.filter_by(id = request.urlvars['id']).first()
        c.current_campaign.status = 2
        meta.Session.commit()
        h.redirect(url(controller='campaign', action='index'))

    def end(self):
        """Завершение кампании - окончена, неактивна"""
        campaign_q = meta.Session.query(model.Campaign)
        c.current_campaign = campaign_q.filter_by(id = request.urlvars['id']).first()
        c.current_campaign.status = 3
        meta.Session.commit()
        h.redirect(url(controller='campaign', action='index'))
    
    def assign_globals(self):
        """Инициализация глобальных переменных"""
        campaign_q = meta.Session.query(model.Campaign)
        c.current_campaign = campaign_q.filter_by(status = '1').first()
        app_globals.current_campaign_id = c.current_campaign.id
        app_globals.current_campaign_start_date = c.current_campaign.start_date
        app_globals.current_campaign_end_date = c.current_campaign.end_date
        h.redirect(url(controller='campaign', action='index'))
    
    def info(self):
        """Вывод детальной информации о кампаниях"""
        pass
    
    def settings(self):
        """Настройка параметров:
            Нужды
            Источники финансирования
            Единица измерения"""
            
        finsource_q = meta.Session.query(model.FinSource)
        c.available_finsource = [(finsource.id, finsource.name) for finsource in finsource_q]     
        needs_q = meta.Session.query(model.Needs)
        c.available_needs = [(needs.id, needs.name) for needs in needs_q]
        unit_q = meta.Session.query(model.Unit)
        c.available_units = [(unit.id, unit.name) for unit in unit_q]
        
        return render('/derived/campaign/settings.html')
    
    def limits(self):
        """Настройка лимитов для текущей кампании"""
        pass
    