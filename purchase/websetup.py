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
    
    users.group_create(u"SOTO-50")
    users.group_create(u"OLM-15")
    users.group_create(u"admin")
    
    users.user_create("admin", password="admin")
    users.user_add_role("admin", role="admin")
    users.user_set_group("admin", group="admin")
    
    users.user_create("boss1", password="boss")
    users.user_add_role("boss1", role="boss")
    users.user_set_group("boss1", group="SOTO-50")
    
    users.user_create("boss2", password="boss")
    users.user_add_role("boss2", role="boss")
    users.user_set_group("boss2", group="OLM-15")
    
    users.user_create("director", password="director")
    users.user_add_role("director", role="director")
    users.user_set_group("director", group="admin")
    
    users.user_create("user1", password="user1")
    users.user_add_role("user1", role="user")
    users.user_set_group("user1", group="SOTO-50")
    
    users.user_create("user2", password="user2")
    users.user_add_role("user2", role="user")
    users.user_set_group("user2", group="SOTO-50")
    
    users.user_create("user3", password="user3")
    users.user_add_role("user3", role="user")
    users.user_set_group("user3", group="OLM-15")
    
    users.user_create("user4", password="user4")
    users.user_add_role("user4", role="user")
    users.user_set_group("user4", group="OLM-15")
    
    
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
    
    # Adding items
    log.info("Adding items...")
    item_1 = model.Item()
    item_1.brand = u'Palit'
    item_1.model = u'Radeon 9600'
    item_1.description = u'DVI TV In/Out 128Mb'
    item_1.section_id = '6'
    item_1.unit_id = '1'
    item_1.price = '3500'
    meta.Session.add(item_1)
    meta.Session.flush()
    
    item_2 = model.Item()
    item_2.brand = u'Sapphire'
    item_2.model = u'Geforce 8800GT'
    item_2.description = u'512Mb <PCI-E> DDR-3 ZOTAC'
    item_2.section_id = '6'
    item_2.unit_id = '1'
    item_2.price = '4500'
    meta.Session.add(item_2)
    meta.Session.flush()

    item_3 = model.Item()
    item_3.brand = u'Intel'
    item_3.model = u'Core 2 Duo E7500'
    item_3.description = u'2.93ГГц, 3МБ, FSB 1066МГц, LGA775, OEM'
    item_3.section_id = '11'
    item_3.unit_id = '1'
    item_3.price = '3280'
    meta.Session.add(item_3)
    meta.Session.flush()
    
    item_4 = model.Item()
    item_4.brand = u'Intel'
    item_4.model = u'Core i3-2100'
    item_4.description = u'3.10ГГц, 3МБ, LGA1155, OEM'
    item_4.section_id = '11'
    item_4.unit_id = '1'
    item_4.price = '5500'
    meta.Session.add(item_4)
    meta.Session.flush()
    
    item_5 = model.Item()
    item_5.brand = u'Intel'
    item_5.model = u'Core 2 Quad Q9300'
    item_5.description = u'2.50ГГц, 6МБ, FSB 1333МГц, LGA775, ОЕМ'
    item_5.section_id = '11'
    item_5.unit_id = '1'
    item_5.price = '3500'
    meta.Session.add(item_5)
    meta.Session.flush()
    
    log.info("Everything OK...")