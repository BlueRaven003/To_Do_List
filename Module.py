import time
import pickle as pk
import os


class NoteManager:
    
    def __init__(self, filename='to_do_list/notebook.pkl'):
        self.filename = filename
        self.notes = self.load_notes()
        self.time = time.ctime() 
            
    # load information in notebook.pkl
    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                return pk.load(f)
        return []
    
    # save information in notebook.pkl
    def save_notes(self):
        with open(self.filename, 'wb') as f:
            return pk.dump(self.notes, f)  
             
    def add_note(self, subject: str, text: str):
        note = {'note_id': len(self.notes)+1,
                'subject': subject,
                'text': text,
                'datetime': self.time}
        self.notes.append(note) 
        self.save_notes()
        print(f'\n{note}\nAdded succesfully!')
          
    def delete_note(self, note_id: int):
        for note in self.notes:
            if note['note_id'] == note_id:
                self.notes.remove(note)
                self.save_notes()
                return print(f'\n{note}\nDeleted succesfully!')
        else:
            return print('\nNote not found!')
        
    def edit_note(self, note_id: int, new_subject: str, new_text: str):
        for note in self.notes:
            if note['note_id'] == note_id:
                note.update({'subject': new_subject,
                             'text': new_text,
                             'datetime': self.time})
                self.save_notes()
                return print(f'\n{note}\nChanged succesfully!')
        else:
            return print('\nNote not found!')   
    
    def list_notes(self):
        print('______')
        for note in self.notes:
            print(note) 
        print('______', '\nEnd list')
  
        
def is_number(note_id):
    if note_id.isdigit():
        return True
    else:
        return False
