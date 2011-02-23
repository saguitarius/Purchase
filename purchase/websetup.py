"""Setup the Purchase application"""
## -*- coding: utf-8 -*-
import logging

import pylons.test

from purchase.config.environment import load_environment
from purchase.model.meta import Session, Base

import os.path
from purchase import model
from purchase.model import meta

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup purchase here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    Base.metadata.bind = Base.engine
    Base.metadata.create_all(bind=Session.bind)

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
    
    log.info("Adding units...")
    unit_1 = model.Unit()
    unit_1.name = u'шт.'
    meta.Session.add(unit_1)
    meta.Session.flush()
    
    log.info("Adding items...")
    item_1 = model.Item()
    item_1.brand = u'Palit'
    item_1.model = u'Radeon 9600'
    item_1.description = u'Хорошо горит'
    item_1.section_id = '6'
    item_1.unit_id = '1'
    item_1.price = '3500'
    meta.Session.add(item_1)
    meta.Session.flush()
    
    item_2 = model.Item()
    item_2.brand = u'Sapphire'
    item_2.model = u'Geforce 8800GT'
    item_2.description = u'Ничё так'
    item_2.section_id = '6'
    item_2.unit_id = '1'
    item_2.price = '4500'
    meta.Session.add(item_2)
    meta.Session.flush()
    
    log.info("Everything OK...")