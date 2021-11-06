# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 16:44:42 2021

@author: GHonem
"""


import datetime


last_id = 0

class Note:
    
    def __init__(self, memo, creation_date= datetime.date.today(), tag= ''):
        
        self.memo = memo
        self.creation_date = creation_date
        self.tag = tag
        
        # use last_id from put the class
        global last_id
        
        last_id +=  1
        self.id = last_id
        
        
    def match_memo(self, memo_filter):
        return memo_filter in self.memo
    

    def match_tag(self, tag_filter):
        return tag_filter in self.tag



class Notebook:

    def __init__(self):
        self.notes = []

        
    def new_note(self, memo, creation_date= datetime.date.today(), tag= ''):
        note = Note(memo, creation_date , tag)
        self.notes.append(note)
    
    # underscore means it's for internal use only
    def _find_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        self._find_note(note_id).memo = memo 

    def modify_tags(self, note_id, tag):
        self._find_note(note_id).tag = tag 

    def modify_creation_date(self, note_id, creation_date):
        self._find_note(note_id).creation_date = creation_date
        
    def search(self, filter ):
        return [note for note in self.notes if note.match_memo(filter)]



