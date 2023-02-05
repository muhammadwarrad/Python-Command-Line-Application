from   model  import *
db.connect()
db.drop_tables([Note])
db.create_tables([Note])

note1 = Note(title='Note 1', content='first note blah.')
note2 = Note(title='Note 2', content='fire noteee')
note1.save()
note2.save()