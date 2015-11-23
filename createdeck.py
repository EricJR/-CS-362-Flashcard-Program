#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
###Implemeted some tests to see whether or not tkinter is correctly working.
#Still need to save deck information to a text file and create deck objects.
#Still need to implement a pop up message stating that the newly created deck was succesfully created

#Enter Flashcard Deck Name


#IMPORTS:
#-----------------
import os
import sys
import os.path

import tkinter as tk
import tkinter
from tkinter import *
#-----------------

#Flash Cards array:
flashCards = []

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

        #http://stackoverflow.com/questions/15306631/how-tocreate-children-windows-using-python-tkinter
        #http://stackoverflow.com/questions/15008359/python-3-and-tkinter-opening-new-window-by-clicking-the-button
        #http://www.python-course.eu/tkinter_message_widget.php
    def createWidgets(self):
        self.master.title("Create Deck")
        self.master.geometry("400x400")
        self.master.config(cursor='dot')

        self.deckName = tk.Message(self)
        self.deckName.pack(side="top")

        #Variable for user's preferred deck name
        self.usertext = StringVar()

        Label(self.deckName, text="Enter FlashCard Deck Name").grid(row=0)

        self.e1 = tk.Entry(self.deckName,textvariable = self.usertext)
        self.e1.grid(row=0, column=1)

        #User needs to click save deck#
        self.button = Button(self.deckName,text ="Save Deck",command = self.printMessage)
        self.button.grid(row = 1, column = 1)
        #e1.insert(10,"DeckName")

        self.goBack = tk.Button(self)
        self.goBack["text"] = "Go back to main menu"
        self.goBack["font"] = 'Helvetica 14 bold italic'  ##Sets style, size, bold, italic
        #self.goBack["command"] = self.goBackMenu()
        self.goBack.pack(side="top")

        #self.newCard["command"] = root.destroy

        self.QUIT = tk.Button(self, text="Quit Program", fg="red", font="Helvetica 14 bold italic", command=root.destroy)
        self.QUIT.pack(side="bottom")

    #Used just to test whether or not the input entered into the textbox is being correctly read by the program.
    def printMessage(self):
        print("Name of Newly Created Deck: ", self.usertext.get())


root = tk.Tk()
app = Application(master=root)
app.mainloop()

