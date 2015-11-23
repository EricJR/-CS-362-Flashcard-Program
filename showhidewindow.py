#!/usr/local/bin/python3

#IMPORTANT NOTE READ BELOW
#########see def create(self): to see the hiding window and reappearing window#############

#Team: Syntax Error
#Project: flashCards.py
#Compiler: Python3
#Program Description: 

#tkinter to exe: https://www.youtube.com/watch?v=XctDhMHQlj0

#IMPORTS:
#-----------------
import os
import sys      
import os.path  #Used to read / write files
import re       #Used for regular expressions (Predefined flashcards)
                #Used for GUI  //https://www.youtube.com/watch?v=uh6AdDX7K7U
                #Library to download: http://www.tcl.tk/software/tcltk/download.html
import tkinter as tk
import tkinter
from tkinter import *

#-----------------

#Flash Cards array:
flashCards = []

#Trying to immitate this guys GUI for the question/answer insertion
#https://www.youtube.com/watch?v=9hBIkY8QD88

# def insert():
#     question_i = question.get()
#     answer_i = answer.get()
#     for item in lis: list.insert(END, item)
#     file.close()

def get_new_win(windowTitle):

    NewWin = tk.Toplevel(root)
    NewWin.title(windowTitle)
    NewWin.geometry('400x400')
   
    
#the insert button
#ibutton = Button(root, text = "Launch Insert Window", command = insert_window)

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
        #http://stackoverflow.com/questions/15306631/how-tocreate-children-windows-using-python-tkinter
        #http://stackoverflow.com/questions/15008359/python-3-and-tkinter-opening-new-window-by-clicking-the-button
        #http://www.python-course.eu/tkinter_message_widget.php
    def createWidgets(self):
        self.master.title("Team Syntax Error's Flash Card Program ¯\_(ツ)_/¯") # ¯\_(シ)_/¯
        self.master.geometry("400x400")
        self.master.config(cursor='dot')
        
    # self.lol = tk.Message(self)
       # self.lol
        
        self.hi_there = tk.Message(self)
        #self.hi_there["cursor"] = 'dot'     #Cursor changes to a dot when you hover over 'Flash Card Program'
        self.hi_there["text"] = "\nFlash Card Program!\n"
        #self.hi_there["anchor"] = 'n'
        self.hi_there["fg"] = 'blue'                        ##Changes font color
        self.hi_there["font"] = 'Helvetica 14 bold italic'  ##Sets style, size, bold, italic
        #self.hi_there["bg"] = 'black'                      ##Changes background color
        self.hi_there.pack(side="top")
       
        self.newCard = tk.Button(self)
        self.newCard["text"] = "Create New Flashcard Deck!"
        self.newCard["font"] = 'Helvetica 14 bold italic'  ##Sets style, size, bold, italic
        self.newCard["command"] = self.create
        self.newCard.pack(side="top")
        
        #self.newCard["command"] = root.destroy
        
        self.viewCard = tk.Button(self)
        self.viewCard["text"] = "View Flashcard Deck!"
        self.viewCard["font"] = 'Helvetica 14 bold italic'  ##Sets style, size, bold, italic
        self.viewCard["command"] = self.view
        self.viewCard.pack(side="top")
        #self.viewCard["command"] = root.destroy
        
        self.editCard = tk.Button(self)
        self.editCard["text"] = "Edit Flashcard Deck!"
        self.editCard["font"] = 'Helvetica 14 bold italic'  ##Sets style, size, bold, italic
        self.editCard["command"] = self.edit
        self.editCard.pack(side="top")
        #self.editCard["command"] = root.destroy
          
        self.deleteCard = tk.Button(self)
        self.deleteCard["text"] = "Delete Flashcard Deck!"
        self.deleteCard["font"] = 'Helvetica 14 bold italic'  ##Sets style, size, bold, italic
        self.deleteCard["command"] = self.delete
        self.deleteCard.pack(side="top")
        #self.deleteCard["command"] = root.destroy
                                           
        self.QUIT = tk.Button(self, text="Quit Program", fg="red", font="Helvetica 14 bold italic", command=root.destroy)
        self.QUIT.pack(side="bottom")
        

    def say_hi(self):
        print("Welcome to the flash card program!")
    def create(self): 
        #http://effbot.org/tkinterbook/entry.htm
        #hide window http://stackoverflow.com/questions/1406145/how-do-i-get-rid-of-python-tkinter-root-window
        #call two commands http://stackoverflow.com/questions/5839517/tkinter-call-two-functions
        print("Creating Deck")
        
        def destroying():
            newDeck.destroy() #destroys deck creation window
            root.deiconify()  #Makes the main menu reappear
        
        newDeck = Toplevel()
        root.withdraw()       #this hides the main menu
        newDeck.title = "Title"
        button = Button(newDeck, text="Back to Main Menu", command=destroying)
        button.pack()

    def view(self):
        print("Viewing Deck")
    def edit(self):
        print("Select a Deck")
    def delete(self):
        print("Select a Deck to delete: ")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

#Patch Notes: Example added 
