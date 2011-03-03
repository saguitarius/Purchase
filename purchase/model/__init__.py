"""The application's model objects"""
from purchase.model.meta import Session, Base
from purchase.model import meta

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy import schema, types
import datetime

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
)

unit_table = schema.Table('unit', meta.Base.metadata,
    schema.Column('id', types.Integer(), schema.Sequence('unit_seq_id', optional=True), primary_key=True),
    schema.Column('name', types.Unicode(255)),
)
                          
class Section(object):
    pass

class Item(object):
    pass

class Unit(object):
    pass

orm.mapper(Unit, unit_table)
orm.mapper(Item, item_table)
orm.mapper(Section, section_table, properties={
    'sections':orm.relation(Section, remote_side = [section_table.c.parent_section_id], cascade='all'),
    'items':orm.relation(Item, backref='section', cascade='all'),
})