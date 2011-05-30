## -*- coding: utf-8 -*-

"""The application's model objects"""
from purchase.model.meta import Session, Base
from purchase.model import meta

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy import schema, types
import datetime

from authkit.users.sqlalchemy_04_driver import setup_model

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    #Session.configure(bind=engine)
    sm = orm.sessionmaker(autoflush=True, autocommit=False, bind=engine)
    meta.Base.engine = engine
    meta.Session = orm.scoped_session(sm)
    
def now():
    return datetime.datetime.now()
    
section_table = schema.Table('section', meta.Base.metadata,
    schema.Column('id', types.Integer(), schema.Sequence('section_seq_id', optional=True), primary_key=True),
    schema.Column('name', types.Unicode(255)),
    schema.Column('description', types.Unicode(255), default=u''),
    schema.Column('parent_section_id', types.Integer, schema.ForeignKey('section.id'), nullable=True),
    schema.Column('created', types.DateTime(), default=now),
    schema.Column('edited', types.DateTime(), default=now),
)

item_table = schema.Table('item', meta.Base.metadata,
    schema.Column('id', types.Integer(), schema.Sequence('item_seq_id', optional=True), primary_key=True),
    schema.Column('brand', types.Unicode(255)),
    schema.Column('model', types.Unicode(255)),
    schema.Column('description', types.Unicode(255)),
    schema.Column('section_id', types.Integer, schema.ForeignKey('section.id'), nullable=True),
    schema.Column('unit_id', types.Integer, schema.ForeignKey('unit.id'), nullable=True),
    schema.Column('price', types.Integer, default=0),
    schema.Column('created', types.DateTime(), default=now),
    schema.Column('edited', types.DateTime(), default=now),
    schema.Column('deleted', types.Integer, default=0),
)

unit_table = schema.Table('unit', meta.Base.metadata,
    schema.Column('id', types.Integer(), schema.Sequence('unit_seq_id', optional=True), primary_key=True),
    schema.Column('name', types.Unicode(255)),
)

app_table = schema.Table('app', meta.Base.metadata,
    schema.Column('id', types.Integer(), schema.Sequence('app_seq_id', optional=True), primary_key=True),
    schema.Column('author_id', types.Integer, schema.ForeignKey('users.uid'), nullable=True),
    schema.Column('status', types.Integer()),
    schema.Column('campaign_id', types.Integer, schema.ForeignKey('campaign.id'), nullable=True),
    schema.Column('info', types.Unicode(255)),
    schema.Column('created', types.DateTime(), default=now),
    schema.Column('edited', types.DateTime(), default=now),
)

app_elements_table = schema.Table('app_elements', meta.Base.metadata,
    schema.Column('id', types.Integer(), schema.Sequence('app_elements_seq_id', optional=True), primary_key=True),
    schema.Column('app_id', types.Integer, schema.ForeignKey('app.id'), nullable=True),
    schema.Column('item_id', types.Integer, schema.ForeignKey('item.id'), nullable=True),
    schema.Column('itemp_id', types.Integer, schema.ForeignKey('item.id'), nullable=True),
    schema.Column('quarter1', types.Integer()),
    schema.Column('quarter2', types.Integer()),
    schema.Column('quarter3', types.Integer()),
    schema.Column('quarter4', types.Integer()),
    schema.Column('quarter1p', types.Integer()),
    schema.Column('quarter2p', types.Integer()),
    schema.Column('quarter3p', types.Integer()),
    schema.Column('quarter4p', types.Integer()),
    schema.Column('amount', types.Integer()),
    schema.Column('amountp', types.Integer()),
    schema.Column('price', types.Integer()),
    schema.Column('pricep', types.Integer()),
    schema.Column('finsource', types.Integer, schema.ForeignKey('finsource.id'), nullable=True),
    schema.Column('needs', types.Integer, schema.ForeignKey('needs.id'), nullable=True),
    schema.Column('place', types.Integer, schema.ForeignKey('groups.uid'), nullable=True),
    schema.Column('note', types.Unicode(255)),
    schema.Column('status', types.Integer()),
)

finsource_table = schema.Table('finsource', meta.Base.metadata,
    schema.Column('id', types.Integer(), schema.Sequence('finsource_seq_id', optional=True), primary_key=True),
    schema.Column('name', types.Unicode(255)),
)

needs_table = schema.Table('needs', meta.Base.metadata,
    schema.Column('id', types.Integer(), schema.Sequence('needs_seq_id', optional=True), primary_key=True),
    schema.Column('name', types.Unicode(255)),
)

campaign_table = schema.Table('campaign', meta.Base.metadata,
    schema.Column('id', types.Integer(), schema.Sequence('campaign_seq_id', optional=True), primary_key=True),
    schema.Column('start_date', types.Date(), default=now),
    schema.Column('end_date', types.Date()),
    schema.Column('description', types.Unicode(255)),
    schema.Column('status', types.Integer, default=0),
)

limit_table = schema.Table('limit', meta.Base.metadata,
    schema.Column('id', types.Integer(), schema.Sequence('limit_seq_id', optional=True), primary_key=True),
    schema.Column('campaign_id', types.Integer, schema.ForeignKey('campaign.id'), nullable=True),
    schema.Column('group_uid', types.Integer, schema.ForeignKey('groups.uid'), nullable=True),
    schema.Column('limit_value', types.Integer()),
)
                          
class Section(object):
    pass

class Item(object):
    pass

class Unit(object):
    pass

class App(object):
    pass

class AppElements(object):
    pass

class FinSource(object):
    pass

class Needs(object):
    pass

class Campaign(object):
    pass

class Limit(object):
    pass

orm.mapper(Unit, unit_table)

orm.mapper(FinSource, finsource_table)

orm.mapper(Needs, needs_table)

orm.mapper(Limit, limit_table)

orm.mapper(Campaign, campaign_table, properties={
    'apps':orm.relation(App),
})

orm.mapper(Item, item_table, properties={
    'units':orm.relation(Unit, primaryjoin=item_table.c.unit_id==unit_table.c.id),
})

orm.mapper(AppElements, app_elements_table, properties={   
    'items':orm.relation(Item, primaryjoin=app_elements_table.c.item_id==item_table.c.id),     
    #'itemsp':orm.relation(Item, primaryjoin=app_elements_table.c.itemp_id==item_table.c.id),                                                         
    'finsources':orm.relation(FinSource, primaryjoin=app_elements_table.c.finsource==finsource_table.c.id),                                                                                                                               
    'needss':orm.relation(Needs, primaryjoin=app_elements_table.c.needs==needs_table.c.id),
}) 

orm.mapper(App, app_table, properties={
    'elements':orm.relation(AppElements, backref='app', cascade='all'),
})        
                               
orm.mapper(Section, section_table, properties={
    'sections':orm.relation(Section, remote_side = [section_table.c.parent_section_id], cascade='all'),
    'items':orm.relation(Item, backref='section', cascade='all'),
})