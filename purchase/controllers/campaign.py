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
from pylons.decorators import validate
from pylons.decorators.rest import restrict
from sqlalchemy import delete
import datetime

log = logging.getLogger(__name__)

class NewCampaignForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = False
    start_date = formencode.validators.DateConverter(not_empty=True, month_style='dd/mm/yyyy')
    #start_date = formencode.validators.DateValidator(after_now=True)
    end_date = formencode.validators.DateConverter(not_empty=True, month_style='dd/mm/yyyy')
    #end_date = formencode.validators.DateValidator(after_now=True)
    description = formencode.validators.String(not_empty=True)

class CampaignController(BaseController):

    def index(self):
        campaign_q = meta.Session.query(model.Campaign)
        c.current_campaign = campaign_q.filter_by(status = '1').first()
        c.finished_active_campaign = campaign_q.filter_by(status = '2').all()
        c.finished_inactive_campaign = campaign_q.filter_by(status = '3').all()
        return render('/derived/campaign/view.html')
    
    def new(self):
        return render('/derived/campaign/new.html')
    
    """
    Campaign status:
        1 Newly created, current, active
        2 Current, finished, active
        3 Finished, inactive
    """
    
    @validate(schema=NewCampaignForm(), form='new')
    # MUST create a decent validator!
    def create(self):
        "Creates campaign"
        campaign = model.Campaign()
        campaign.start_date = self.form_result['start_date']
        campaign.end_date = self.form_result['end_date']
        campaign.status = '1'
        campaign.description = self.form_result['description']
        meta.Session.add(campaign)
        meta.Session.flush()
        h.redirect(url(controller='campaign', action='assign_globals'))
    
    def assign_globals(self):
        campaign_q = meta.Session.query(model.Campaign)
        c.current_campaign = campaign_q.filter_by(status = '1').first()
        app_globals.current_campaign_id = c.current_campaign.id
        app_globals.current_campaign_start_date = c.current_campaign.start_date
        app_globals.current_campaign_end_date = c.current_campaign.end_date
        h.redirect(url(controller='campaign', action='index'))
    
    def info(self):
        pass
    