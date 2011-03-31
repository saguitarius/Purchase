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

class AppController(BaseController):

    def index(self):
        app_q = meta.Session.query(model.App)
        c.current_app = app_q.filter_by(author_id = app_globals.user_id).filter_by(campaign_id = app_globals.current_campaign_id).first()
        c.all_apps = app_q.filter_by(author_id = app_globals.user_id).all()
        return render('/derived/app/view.html')