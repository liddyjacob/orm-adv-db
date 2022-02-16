# generated using python -m pwiz -e sqlite3 shopping_list.db 
from peewee import *

database = SqliteDatabase('shopping_list.db')

class BaseModel(Model):
    class Meta:
        database = database

class Person(BaseModel):
    name = TextField(null=True)

    class Meta:
        table_name = 'person'

class List(BaseModel):
    description = TextField(null=True)
    person = ForeignKeyField(Person, backref='items')

    class Meta:
        table_name = 'list'