# User enters deck name and deck description. They will then click on Save deck to save the deck information to a text file
# User enters front card information and back card information and click save card to save card to the text file

# Format of newly created deck in textfile will be @@@DeckName~~DeckDescription
# Format of newly created card in textfile will be FrontCardInfo~~BackCardInfo

import os
import sys
import os.path
import tkinter as tk
import tkinter
from tkinter import *
import tkinter.messagebox

# Flash Cards array:
flashCards = []

class switchWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.wm_title(self,"Create Deck")
        #tk.Tk.geometry(self,"400x400")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (createDeck,addCards):

            frame = F(container, self)

            self.frames[F] = frame
        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(createDeck)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        if c == createDeck:
            tk.Tk.wm_title(self,"Create Deck")
        else:
            tk.Tk.wm_title(self,"Add Cards")
        frame = self.frames[c]
        frame.tkraise()

    def quitProgram(self):
        tk.Tk.destroy(self)


# Gets deck name and deck description from user and creates the deck.
# Stores the deck information into a text file
class createDeck(tk.Frame):
    def __init__(self, master,controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        #self.pack()
        self.createWidgets()

    def createWidgets(self):

        # Variable for user's preferred deck name and deck description
        self.usertext = StringVar()
        self.usertext2 = StringVar()

        # Labels for "Enter Deck Name" and "Enter Deck Description"
        Label(self, text="Enter Deck Name").grid(row=0)
        e1 = tk.Entry(self, textvariable=self.usertext)
        e1.grid(row=0, column=1)

        Label(self, text="Enter Deck Description").grid(row=1)
        e2 = tk.Entry(self, textvariable=self.usertext2)
        e2.grid(row=1, column=1)

        # User needs to click save deck
        button = Button(self, text="Save Deck", command=self.printMessage)
        button.grid(row=2, column=1)


    # Print deck to textfile. Display an OK messagebox if successful. Will check if user actually entered deck name and description before writing to file.
    def printMessage(self):
        if len(self.usertext.get()) == 0 and len(self.usertext2.get()) == 0:
            tkinter.messagebox.showinfo("Error", "You need to enter a Deck Name and Description!")
        elif len(self.usertext.get()) == 0:
            tkinter.messagebox.showinfo("Error", "You need to enter a Deck Name!")
        elif len(self.usertext.get()) == 0:
            tkinter.messagebox.showinfo("Error", "You need to enter a Deck Description!")
        else:
            text_file = open("Flashcards.txt", "a")
            text_file.write("@@@" + self.usertext.get() + "~~" + self.usertext2.get() + "\n")
            text_file.close()
            # print("Writing to file...")
            tkinter.messagebox.showinfo("Deck Created!", "Successfully created " + self.usertext.get() + "!")
            self.controller.show_frame(addCards)


class addCards(tk.Frame):
    def __init__(self, master,controller):
        tk.Frame.__init__(self, master)
        #self.pack()
        self.createWidgets()
        self.controller = controller

    def createWidgets(self):

        # Variable for user input for Front and Back of Flashcard
        self.cardFront = StringVar()
        self.backCard = StringVar()

        Label(self, text="Enter Question").grid(row=0)
        self.e1 = tk.Entry(self, textvariable=self.cardFront)
        self.e1.grid(row=0, column=1)

        Label(self, text="Enter Answer").grid(row=1)
        self.e2 = tk.Entry(self, textvariable=self.backCard)
        self.e2.grid(row=1, column=1)

        # User needs to click save deck
        button = Button(self, text="Save Card", command=self.printMessage)
        button.grid(row=2, column=1)

        button2 = Button(self, text="Exit", command=self.quit)
        button2.grid(row=3, column=1)

    #Checks if user entered both front and back information. If they did it will write question and answer to text file.
    def printMessage(self):
        if len(self.cardFront.get()) == 0 and len(self.backCard.get()) == 0:
            tkinter.messagebox.showinfo("Error", "You need to enter a Question and Answer!")
        elif len(self.cardFront.get()) == 0:
            tkinter.messagebox.showinfo("Error", "You need to enter a Question!")
        elif len(self.backCard.get()) == 0:
            tkinter.messagebox.showinfo("Error", "You need to enter an Answer!")
        else:
            text_file = open("Flashcards.txt", "a")
            text_file.write(self.cardFront.get() + "~~" + self.backCard.get() + "\n")
            text_file.close()
            #Delete the Contents of the 2 labels
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            #print("Writing to file...")
            tkinter.messagebox.showinfo("Card Added!", "Successfully added FlashCard to your deck.")

    def quit(self):
        self.controller.quitProgram()

def main():
    app = switchWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
