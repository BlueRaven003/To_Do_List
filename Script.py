import Module

module = Module.NoteManager()

while True:
    command = input('''\n0.exit
1.add_note
2.delete_note
3.edit_note
4.list_notes \n''')
    # exit
    if command == '0':
        print('\nExiting...')
        break
    # add note
    elif command == '1':
        subject = input('subject: ')
        text = input('text: ')
        module.add_note(subject, text)
    # delete note
    elif command == '2':
        note_id = input('note_id: ')
        if Module.is_number(note_id):      
            note_id = int(note_id)    
            module.delete_note(note_id)  
        else:
            print('\nnote_id is not number!')  
    # edit note
    elif command == '3':
        note_id = input('note_id: ')
        if Module.is_number(note_id):   
            note_id = int(note_id)   
            new_subject = input('new_subject: ')
            new_text = input('new_text: ') 
            module.edit_note(note_id, new_subject, new_text)  
        else:
            print('\nnote_id is not number!')
    # print note_list
    elif command == '4':
        module.list_notes()
    # erorr handeling
    else:
        print('\nInvalid command!') 
