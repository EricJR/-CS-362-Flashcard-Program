import tkinter as Tk
import re
import sys
import os
from tkinter import messagebox
from flashcard_classes import *

class MyApp(object):
    """"""
    def __init__(self, parent):
        """Constructor"""
        
        self.root = parent
        self.root.title("Deleting Deck")
        self.frame = Tk.Frame(parent)
        self.frame.pack()
        
        self.deckString = []
        self.index = 0
        
        self.controller = FlashcardController()
        self.file_sys = FileSystemStorage()
        debug = True
    
        # Testing the file system
        self.file_sys.read_from_file(self.controller)

        hi_there = Tk.Message(self.frame)
        hi_there["text"] = "\nWhich Deck to Delete?\n"
        hi_there["width"] = 1000
        hi_there.pack(side = "top")
        
        self.deck_names = []
        self.index = 0
        
        decks = self.controller.get_decks()
        for deck in decks:
            self.deck_names.append(deck.get_name())
            deck_name = deck.get_name()
            self.deck = Tk.Button(self.frame)
            self.deck["text"] = deck_name
            self.deck["command"] = lambda: self.delete(self.deck_names[self.index])
            self.deck.pack(side="top")
            self.index += 1
     
        quit = Tk.Button(self.frame, text="Quit Program", command=root.destroy)
        quit.pack(side = "bottom")

        menu = Tk.Button(self.frame, text="Back to Menu")
        menu.pack(side = "bottom")
        
        
    def delete(self, deck_name):
        self.index -= 3
        print(self.deck_names[self.index]) 
        dialog_title = 'Deletion Confirmation'
        dialog_text = 'Are you sure you want to delete this deck?'
        answer = messagebox.askquestion(dialog_title, dialog_text)
        
        if answer == 'yes':
            self.controller.delete_deck(self.deck_names[self.index])
            self.file_sys.write_to_file(self.controller)
        else:
            return

#----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("700x500")
    app = MyApp(root)
    root.mainloop()
