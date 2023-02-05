from peewee import *

from   model  import *

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

def create_note(title, content):
    new_note = Note(title=title, content=content)
    new_note.save()
    print(f'Note "{title}" created successfully.')

def menu():
    print('Welcome to Notes')
    print('1. all notes')
    print('2. View one note')
    print('3. Create note')
    print('4. Quit')
    
    choice = input('Enter your choice: ')

    if choice == '1':
        list_notes()
    elif choice == '2':
        index = int(input('Enter note index: '))
        view_note(index)
    elif choice == '3':
        title = input('Enter note title: ')
        content = input('Enter note content: ')
        create_note(title, content)
    elif choice == '4':
        print('bye')
        exit()
    
    else:
        print('Error')

menu()