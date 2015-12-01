#User enters deck name and deck description. They will then click on Save deck to save the deck information to a text file
#Format of newly created deck in textfile will be @@@DeckName~~DeckDescription

import os
import sys
import os.path
import tkinter as tk
import tkinter
from tkinter import *
import tkinter.messagebox

# Flash Cards array:
flashCards = []

#Gets deck name and deck description from user and creates the deck.
#Stores the deck information into a text file
class createDeck(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.master.title("Create Deck")
        self.master.geometry("400x400")
        self.master.config(cursor='dot')

        # Variable for user's preferred deck name and deck description
        self.usertext = StringVar()
        self.usertext2 = StringVar()

        # Labels for "Enter Deck Name" and "Enter Deck Description"
        Label(self, text="Enter Deck Name").grid(row=0)
        self.e1 = tk.Entry(self, textvariable=self.usertext)
        self.e1.grid(row=0, column=1)

        Label(self, text="Enter Deck Description").grid(row=1)
        self.e2 = tk.Entry(self, textvariable=self.usertext2)
        self.e2.grid(row=1, column=1)

        # User needs to click save deck
        self.button = Button(self, text="Save Deck", command=self.printMessage)
        self.button.grid(row=2, column=1)


    # Print deck to textfile
    def printMessage(self):
        text_file = open("Flashcards.txt", "a")
        text_file.write("@@@" + self.usertext.get() + "~~" + self.usertext2.get() + "\n")
        text_file.close()
        #print("Writing to file...")
        tkinter.messagebox.showinfo("Deck Created!", "Successfully created " + self.usertext.get() + "!")



root = tk.Tk()
app = createDeck(master=root)
app.mainloop()
