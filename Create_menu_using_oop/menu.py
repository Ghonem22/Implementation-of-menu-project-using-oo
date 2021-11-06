# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 16:45:41 2021

@author: GHonem
"""


import sys
from  utilities import *


class Menu:

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {    "1": self.show_notes,
                            "2": self.search_notes,
                            "3": self.add_note,
                            "4": self.modify_note,
                            "5": self.quit
                        }

    def display_menu(self):
        print("""
                1: show_notes,
                2: search_notes,
                3: add_note,
                4: modify_note,
                5: quit
                
                """)


    def run(self):
        # Display the menu and respond to choices.
        
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            # use choices argument to retrive method
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))


    def show_notes(self, notes = None):
        # disply notes content,
        # if None, display content of all existed notes

        if not notes:
            notes = self.notebook.notes
            
        if not notes:
            print("There is no notes to display")
            return 
        
        for note in notes:
            print("{0}:  {1} \n        creation_date:  {2} \t\t\t tag:  {3} \n".format(
                note.id, note.memo, note.creation_date, note.tag))

    def search_notes(self):
        # display all notes that includes the filter

        filter = input("enter the words that you want to search for: ")
        notes =  self.notebook.search(filter)

        if notes:
            self.show_notes(notes)
        # show_notes return all notes if it took None arguments, so we  make sure that won't happen
        else:
            print("There is no note with these words")


    def add_note(self):
        # add new notr yo our menu

        memo = input("input your  note:  ")
        creation_date = input("input the creation date, press enter to use today date:  ")
        tag = input("input the tag, press enter to leave it blank:  ")

        if not creation_date:
            creation_date= datetime.date.today()


        self.notebook.new_note(memo, creation_date, tag)


    def modify_note(self):
        # modify memo/ creation_date/ tag using  memo id

        id = int(input("input your  note id:  "))
        new_memo = input("input new memo:  ")
        new_creation_date = input("input new creation date:  ")
        new_tag = input("input new tag:  ")

        if  new_memo:
            modify_memo(id, new_memo)

        if new_creation_date:
            modify_creation_date(id, new_creation_date)

        if new_tag:
            modify_tag(id, new_tag)

    def quit(self):
        # exit from run method (while infinite loop)
        print("closing the notebook for today")
        sys.exit(0)
        
        
        
        
if __name__ == "__main__":
    Menu().run()
        
