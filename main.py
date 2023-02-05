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

def list_notes():
    notes = Note.select()
    for i, note in enumerate(notes):
        print(f'{i+1}. {note.title}')
        
def view_note(index):
    notes = Note.select()
    try:
        selected_note = notes[index - 1]
        print(f'Title: {selected_note.title}')
        print(f'Content: {selected_note.content}')
    except IndexError:
        print('Invalid index.')

def menu():
    print('Welcome to Notes')
    print('1. all notes')
    print('2. View one note')
    print('3. Create note')
    print('4. Quit')
    
    choice = input('Enter your choice: ')