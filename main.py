from peewee import *

db = SqliteDatabase('notes.db')

class Note(Model):
    title = CharField()
    content = TextField()
    
    class Meta:
        database = db
        