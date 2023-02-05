from peewee import *

db = SqliteDatabase('notes.db')

class Note(Model):
    title = CharField()
    content = TextField()
    
    class Meta:
        database = db
        
def create_tables():
    db.connect()
    db.create_tables([Note], safe=True)

def seed_data():
    note1 = Note(title='Note 1', content='first note blah.')
    note2 = Note(title='Note 2', content='fire noteee')
    note1.save()
    note2.save()