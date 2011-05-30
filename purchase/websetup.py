"""Setup the Purchase application"""
## -*- coding: utf-8 -*-
import logging

import pylons.test

from purchase.config.environment import load_environment
from purchase.model.meta import Session, Base

import os.path
from purchase import model
from purchase.model import meta

from authkit.users.sqlalchemy_driver import UsersFromDatabase

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup purchase here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)
    
    # Auth tables
    log.info("Adding the AuthKit model...")
    users = UsersFromDatabase(model)

    # Create the tables if they don't already exist
    Base.metadata.bind = Base.engine
    Base.metadata.create_all(bind=Session.bind)

    # Adding users, groups, roles
    users.role_create("admin")
    users.role_create("boss")
    users.role_create("director")
    users.role_create("user")
    
    users.group_create(u"admin")
    users.group_set_view(u"admin", u"Администрация")
    users.group_create(u"SOTO-50")
    users.group_set_view(u"SOTO-50", u"СОТО-50")
    users.group_create(u"OLM-15")
    users.group_set_view(u"OLM-15", u"ОЛМ-15")
    
    users.user_create("admin", password="admin")
    users.user_set_view("admin", u'Администратор')
    users.user_add_role("admin", role="admin")
    users.user_set_group("admin", group="admin")
    
    users.user_create("boss1", password="boss")
    users.user_set_view("boss1", u'Ответственный по подразделению')
    users.user_add_role("boss1", role="boss")
    users.user_set_group("boss1", group="SOTO-50")
    
    users.user_create("boss2", password="boss")
    users.user_set_view("boss2", u'Ответственный по подразделению')
    users.user_add_role("boss2", role="boss")
    users.user_set_group("boss2", group="OLM-15")
    
    users.user_create("director", password="director")
    users.user_set_view("director", u'Ответственный по предприятию')
    users.user_add_role("director", role="director")
    users.user_set_group("director", group="admin")
    
    users.user_create("user1", password="user1")
    users.user_set_view("user1", u'Иванов Иван Иванович')
    users.user_add_role("user1", role="user")
    users.user_set_group("user1", group="SOTO-50")
    
    users.user_create("user2", password="user2")
    users.user_set_view("user2", u'Петров Пётр Петрович')
    users.user_add_role("user2", role="user")
    users.user_set_group("user2", group="SOTO-50")
    
    users.user_create("user3", password="user3")
    users.user_set_view("user3", u'Семёнов Семён Семёнович')
    users.user_add_role("user3", role="user")
    users.user_set_group("user3", group="OLM-15")
    
    users.user_create("user4", password="user4")
    users.user_set_view("user4", u'Сергеев Сергей Сергеевич')
    users.user_add_role("user4", role="user")
    users.user_set_group("user4", group="OLM-15")
    
#    # Adding campaign
#    campaign = model.Campaign()
#    campaign.start_date = '2011.05.20'
#    campaign.end_date = '2011.05.30'
#    campaign.status = '1'
#    campaign.description = u'Тестовая кампания'
#    meta.Session.add(campaign)
#    meta.Session.flush()
    
    # Adding units
    log.info("Adding units...")
    unit_1 = model.Unit()
    unit_1.name = u'шт.'
    meta.Session.add(unit_1)
    meta.Session.flush()
    
    # Adding needs
    log.info("Adding needs...")
    needs_1 = model.Needs()
    needs_1.name = u'Закупка нового'
    meta.Session.add(needs_1)
    meta.Session.flush()    

    needs_2 = model.Needs()
    needs_2.name = u'Обновление старого'
    meta.Session.add(needs_2)
    meta.Session.flush()  
    
    # Adding finsources
    log.info("Adding finsources...")
    finsource_1 = model.FinSource()
    finsource_1.name = u'Накладные расходы'
    meta.Session.add(finsource_1)
    meta.Session.flush()    
    
    finsource_2 = model.FinSource()
    finsource_2.name = u'Тема №1'
    meta.Session.add(finsource_2)
    meta.Session.flush()        
    
    finsource_3 = model.FinSource()
    finsource_3.name = u'Тема №2'
    meta.Session.add(finsource_3)
    meta.Session.flush()  
    
    # Adding sections
    log.info("Adding main sections...")
    section_home = model.Section()
    section_home.name = u'Главная'
    section_home.parent_section_id = None
    meta.Session.add(section_home)
    meta.Session.flush()
    
    section_components= model.Section()
    section_components.name = u'Компоненты'
    section_components.parent_section_id = '1'
    meta.Session.add(section_components)
    meta.Session.flush()
    
    section_hard_drives= model.Section()
    section_hard_drives.name = u'Жёсткие диски'
    section_hard_drives.parent_section_id = '1'
    meta.Session.add(section_hard_drives)
    meta.Session.flush()
    
    section_printers_scanners= model.Section()
    section_printers_scanners.name = u'Принтеры и сканеры'
    section_printers_scanners.parent_section_id = '1'
    meta.Session.add(section_printers_scanners)
    meta.Session.flush()
   
    section_memory = model.Section()
    section_memory.name = u'Память'
    section_memory.parent_section_id = '2'
    meta.Session.add(section_memory)
    meta.Session.flush()
    
    section_video_cards = model.Section()
    section_video_cards.name = u'Видеокарты'
    section_video_cards.parent_section_id = '2'
    meta.Session.add(section_video_cards)
    meta.Session.flush()
    
    section_processors = model.Section()
    section_processors.name = u'Процессоры'
    section_processors.parent_section_id = '2'
    meta.Session.add(section_processors)
    meta.Session.flush()
    
    section_printers = model.Section()
    section_printers.name = u'Принтеры'
    section_printers.parent_section_id = '4'
    meta.Session.add(section_printers)
    meta.Session.flush()
    
    section_scanners = model.Section()
    section_scanners.name = u'Сканеры'
    section_scanners.parent_section_id = '4'
    meta.Session.add(section_scanners)
    meta.Session.flush()
    
    section_ink_toner = model.Section()
    section_ink_toner.name = u'Чернила и тонеры'
    section_ink_toner.parent_section_id = '4'
    meta.Session.add(section_ink_toner)
    meta.Session.flush()
    
    section_intel = model.Section()
    section_intel.name = u'Intel'
    section_intel.parent_section_id = '7'
    meta.Session.add(section_intel)
    meta.Session.flush()
    
    section_amd = model.Section()
    section_amd.name = u'AMD'
    section_amd.parent_section_id = '7'
    meta.Session.add(section_amd)
    meta.Session.flush()

    
    log.info("Everything OK...")