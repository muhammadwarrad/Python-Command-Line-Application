from peewee import *

db = PostgresqlDatabase('notes2', user='postgres', password='12345', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Note( BaseModel):
    title = CharField()
    content = CharField()
         
