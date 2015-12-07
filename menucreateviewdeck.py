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

#mainFileSys.read_from_file(mainController)

#Helps "switch" windows by hiding windows and raising desired window
class switchWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.wm_title(self,"Create Deck")
        tk.Tk.geometry(self,"400x400")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Application,createDeck,addCards,viewCards):

            frame = F(self.container, self)

            self.frames[F] = frame
        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Application)

    #Used to show the desired frame.  Will name the frame based on the class
    def show_frame(self, c):
        '''Show a frame for the given class'''
        if c == Application:
            tk.Tk.wm_title(self,"Team Syntax Error's Flash Card Program")
        elif c == createDeck:
            tk.Tk.wm_title(self,"Create Deck")
        elif c == viewCards:
            tk.Tk.wm_title(self,"View Cards")
            for F in (Application,createDeck,addCards,viewCards):

                frame = F(self.container, self)

                self.frames[F] = frame
        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
                frame.grid(row=0, column=0, sticky="nsew")
        else:
            tk.Tk.wm_title(self,"Add Cards")
        frame = self.frames[c]
        frame.tkraise()

    #Quit the program
    def quitProgram(self):
        tk.Tk.destroy(self)


class Application(tk.Frame):
    def __init__(self, master,controller):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.controller = controller
        #http://stackoverflow.com/questions/15306631/how-tocreate-children-windows-using-python-tkinter
        #http://stackoverflow.com/questions/15008359/python-3-and-tkinter-opening-new-window-by-clicking-the-button
        #http://www.python-course.eu/tkinter_message_widget.php
    def createWidgets(self):
        #self.master.title("Team Syntax Error's Flash Card Program")
        #self.master.geometry("400x400")
        #self.master.config(cursor='dot')

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

        self.QUIT = tk.Button(self, text="Quit Program", fg="red", font="Helvetica 14 bold italic", command=self.quit)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("Welcome to the flash card program!")
    def create(self):
        self.controller.show_frame(createDeck)
    def view(self):
        self.controller.show_frame(viewCards)
    def edit(self):
        print("Select a Deck")
    def delete(self):
        print("Select a Deck to delete: ")

    def quit(self):
        self.controller.quitProgram()

#User will enter Question and Answer. After user presses exit, the cards along with the deck name and description will be saved to the text file
#Format of newly created deck in textfile will be @@@DeckName~~DeckDescription
#Format of newly created card in textfile will be Question~~Answer
class createDeck(tk.Frame):
    def __init__(self, master,controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.createWidgets()

    def goBack(self):
        self.controller.show_frame(Application)

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

        #Go back to main menu
        button2 = Button(self, text="Go back to Main Menu", command=self.goBack)
        button2.pack()

        #Exit button
        button3 = Button(self, text="Exit", command=self.quit)
        button3.pack()

        #Status Bar
        self.status = Label(self,text="Create your Deck",bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM,fill=X)

    # Print deck to textfile. Display an OK messagebox if successful. Will check if user actually entered deck name and description before saving to controller.
    def saveContents(self):
        global mainController
        global deckName

        #delete previous status
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
            #Delete contents in entries
            self.e1.delete(0,END)
            self.e2.delete(0,END)


#User will enter Question and Answer. After user presses exit, the cards along with the deck name and description will be saved to the text file
# Format of newly created deck in textfile will be @@@DeckName~~DeckDescription
# Format of newly created card in textfile will be Question~~Answer
class addCards(tk.Frame):
    def __init__(self, master,controller):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.controller = controller

    def goBack(self):
        self.controller.show_frame(Application)
        #Will save the deck name if the user just chooses to go back to the main menu
        mainFileSys.write_to_file(mainController)

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

        #Go back to Main Menu
        button2 = Button(self, text="Go Back to Main Menu", command = self.goBack)
        button2.pack()

        #Exit button
        button3 = Button(self, text="Exit", command=self.quit)
        button3.pack()

        #Status Bar
        self.status = Label(self,text="Add Cards to your Deck",bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM,fill=X)

    #Checks if user entered both front and back information. If they did it will write question and answer to text file.
    def saveContents(self):
        global mainController
        global deckName
        global mainFileSys

        #Erase old status
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
            #Delete previous entries so user can add more cards if they want
            self.e1.delete(0,END)
            self.e2.delete(0,END)

            self.status = Label(self,text="Flashcard successfully added to your Deck!",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)

    #Quit Program will save the contents.
    def quit(self):
        mainFileSys.write_to_file(mainController)
        self.controller.quitProgram()

#View Flashcards
class viewCards(tk.Frame):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, master,controller):
        item = tk.Frame.__init__(self, master)
        self.controller = controller
        self.createWidgets()

    def createWidgets(self):
        global mainController
        global mainFileSys
        #self.root = parent
        #self.root.title("Main frame")
        #self.frame = Tk.Frame(parent)
        #self.frame.pack()

        self.questionString = []
        self.answerString = []
        self.index = 0
        #debug = True

        # Testing the file system
        mainFileSys.read_from_file(mainController)

        decks = mainController.get_decks()
        for deck in decks:
            cards = deck.get_cards()
            for card in cards:
                self.questionString.append(card.get_term())
                self.answerString.append(card.get_definition())

        print("Length qstring = ", len(self.questionString))

        if(len(self.questionString) == 0):
            hi_there = tk.Message(self)
            hi_there["text"] = "\nDeck is Empty!\n"
            hi_there["width"] = 1000
            hi_there.pack(side = "top")

            menu = tk.Button(self, text="Back to Menu",command=self.goBack)
            menu.pack(side = "bottom")

        else:
            hi_there = tk.Message(self)
            hi_there["text"] = "\nNow Viewing Deck!\n"
            hi_there["width"] = 1000
            hi_there.pack(side = "top")

            self.questionGUI = tk.Message(self)
            self.questionGUI["fg"] = 'black'
            self.questionGUI["width"] = 600
            self.questionGUI["text"] = self.questionString[self.index] + "\n"
            self.questionGUI.pack(side = "top")

            self.answerGUI = tk.Message(self)
            self.answerGUI["fg"] = 'white'
            self.answerGUI["width"] = 600
            self.answerGUI["text"] = self.answerString[self.index] + "\n"
            self.answerGUI.pack(side = "top")

            answer = tk.Button(self, text="Flip")
            answer["command"] = lambda: self.openFrame()
            answer.pack(side = "top")

            previousCard = tk.Button(self, text="Previous Card")
            previousCard["command"] = lambda : self.decrementIndex()
            previousCard.pack(side = "left")

            nextCard = tk.Button(self, text="Next Card")
            nextCard["command"] = lambda : self.incrementIndex()
            nextCard.pack(side = "right")

            quit = tk.Button(self, text="Quit Program", command=self.quit)
            quit.pack(side = "bottom")

            menu = tk.Button(self, text="Back to Menu",command=self.goBack)
            menu.pack(side = "bottom")

    def incrementIndex(self):
        self.index += 1

        if (self.index == len(self.questionString)):
            self.index = len(self.questionString) - 1
        else:
            self.questionGUI["text"] = self.questionString[self.index] + "\n"
            self.questionGUI.pack(side = "top")

            self.answerGUI["text"] = self.answerString[self.index] + "\n"
            self.answerGUI.pack(side = "top")

    def decrementIndex(self):

        if (self.index == 0):
            self.index = 0
        else:
            self.index -= 1
            self.questionGUI["text"] = self.questionString[self.index] + "\n"
            self.questionGUI.pack(side = "top")

            self.answerGUI["text"] = self.answerString[self.index] + "\n"
            self.answerGUI.pack(side = "top")

    def goBack(self):
            self.controller.show_frame(Application)
    #----------------------------------------------------------------------

    def openFrame(self):
        if self.answerGUI["fg"] == 'white':
            self.answerGUI["fg"] = 'black'
        elif self.answerGUI["fg"] == 'black':
            self.answerGUI["fg"] = 'white'

        if self.questionGUI["fg"] == 'black':
            self.questionGUI["fg"] = 'white'
        elif self.questionGUI["fg"] == 'white':
            self.questionGUI["fg"] = 'black'


def main():
    create = switchWindow()
    create.mainloop()

if __name__ == "__main__":
    main()
