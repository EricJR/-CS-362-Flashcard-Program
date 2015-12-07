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
from flashcard_classes import *

mainController = FlashcardController()
mainFileSys = FileSystemStorage()
deckName = ""

mainFileSys.read_from_file(mainController)

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
        self.deckName = StringVar()
        self.deckDescription = StringVar()

        # Labels for "Enter Deck Name" and "Enter Deck Description"
        Label(self, text="Enter Deck Name").pack()
        self.e1 = tk.Entry(self, textvariable=self.deckName)
        self.e1.pack()

        Label(self, text="Enter Deck Description").pack()
        self.e2 = tk.Entry(self, textvariable=self.deckDescription)
        self.e2.pack()

        # User needs to click save deck
        button = Button(self, text="Save Deck", command=self.saveContents)
        button.pack()

        #Exit button
        button2 = Button(self, text="Exit", command=self.quit)
        button2.pack()

        self.status = Label(self,text="Create your Deck",bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM,fill=X)

    # Print deck to textfile. Display an OK messagebox if successful. Will check if user actually entered deck name and description before saving to controller.
    def saveContents(self):
        global mainController
        global deckName
        self.status.destroy()

        if len(self.deckName.get()) == 0 and len(self.deckDescription.get()) == 0:
            #tkinter.messagebox.showinfo("Error", "You need to enter a Deck Name and Description!")
            self.status = Label(self,text="Error: You need to enter a Deck Name and Description!",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        elif len(self.deckName.get()) == 0:
            #tkinter.messagebox.showinfo("Error", "You need to enter a Deck Name!")
            self.status = Label(self,text="Error: You need to enter a Deck Name!",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        elif len(self.deckDescription.get()) == 0:
            #tkinter.messagebox.showinfo("Error", "You need to enter a Deck Description!")
            self.status = Label(self,text="Error: You need to enter a Deck Description!",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        else:
            deckName = self.deckName.get()
            mainController.new_deck(self.deckName.get(),self.deckDescription.get())
            tkinter.messagebox.showinfo("Deck Created!", "Successfully created " + self.deckName.get() + "!")
            self.controller.show_frame(addCards)
            self.e1.delete(0,END)
            self.e2.delete(0,END)

class addCards(tk.Frame):
    def __init__(self, master,controller):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.controller = controller

    def goBack(self):
        self.controller.show_frame(createDeck)

    def createWidgets(self):

        # Variable for user input for Front and Back of Flashcard
        self.cardFront = StringVar()
        self.backCard = StringVar()

        Label(self, text="Enter Question").pack()
        self.e1 = tk.Entry(self, textvariable=self.cardFront)
        self.e1.pack()

        Label(self, text="Enter Answer").pack()
        self.e2 = tk.Entry(self, textvariable=self.backCard)
        self.e2.pack()

        # User needs to click save deck
        button = Button(self, text="Save Card", command=self.saveContents)
        button.pack()

        button2 = Button(self, text="Go Back to Create Deck", command = self.goBack)
        button2.pack()

        #Exit button
        button3 = Button(self, text="Exit", command=self.quit)
        button3.pack()

        self.status = Label(self,text="Add Cards to your Deck",bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM,fill=X)

    #Checks if user entered both front and back information. If they did it will write question and answer to text file.
    def saveContents(self):
        global mainController
        global deckName
        global mainFileSys

        self.status.destroy()

        if len(self.cardFront.get()) == 0 and len(self.backCard.get()) == 0:
            #tkinter.messagebox.showinfo("Error", "You need to enter a Question and Answer!")
            self.status = Label(self,text="Error: You need to enter a Question and Answer",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        elif len(self.cardFront.get()) == 0:
            #tkinter.messagebox.showinfo("Error", "You need to enter a Question!")
            self.status = Label(self,text="Error: You need to enter a Question!",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        elif len(self.backCard.get()) == 0:
            #tkinter.messagebox.showinfo("Error", "You need to enter an Answer!")
            self.status = Label(self,text="Error: You need to enter an Answer",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        else:
            for deck in mainController.get_decks():
                if deck.get_name() == deckName:
                    deck.add_card(self.cardFront.get(), self.backCard.get())

            self.e1.delete(0,END)
            self.e2.delete(0,END)
            self.status = Label(self,text="Card Added! Successfully added FlashCard your Deck!",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)

    def quit(self):
        mainFileSys.write_to_file(mainController)
        self.controller.quitProgram()

def main():
    app = switchWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
