#=======1=========2=========3=========4=========5=========6=========7=========8=========9=========0=========1=========2=========3=========4=========5=========6========7**
#Course information
#  Course: CS-362, Software Engineering
#  Assignment: Final Project
#  Due date: 2015-Dec-14
#Project information
#  Project title: Flash Card Program (aka Never Baguette)
#  Purpose: There are a multitude of resources available to students to make flash cards, but our goal with Never Baguette was to expand the user’s capabilities. This
#    program allows those who use it to create flash cards for effective studying.  Users just have to follow simple instructions to create decks of cards. The program
#    will let them view, edit, and delete decks that they make. It saves paper since everything is done on the computer.  This program will assist countless students on
#    their quests for knowledge.
#  Project files: main.py, flashcard_gui.py, flashcard_classes.py, flashcards_file.txt
#Module information
#  Language: Python 3
#  Date last modified: 2015-Dec-14 (cleaned up some comments)
#  Purpose: This module handles the back end of the GUI and file interaction.
#  File name: flashcard_gui.py
#  Status: Complete.
#References and credits
#  Credits: The internet for its vast knowledge of the library tkinter.
#Permissions
#  The source code is free for use by members of the CS-362 class.  Credit this source if you borrow executable statements from this program.  The instructions
#  are free to use, but create your own comments.  The comments are intellectual property.
#
#===== Begin code area ===================================================================================================================================================

__author__ = "Team Syntax Error"
__version__ = "1.0"
__status__ = "Production"

# Imports tkinter for GUI, flashcard_classes for the flashcards
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from flashcard_classes import *

# Our mainController, mainFileSys, and mainDeckName are global variables used throughout the program.
mainController = FlashcardController()
mainFileSys = FileSystemStorage()
mainDeckName = ""

# Read the content from the mainFileSys into the mainController so that the running program has our current deck information in memory.
mainFileSys.read_from_file(mainController)
#=========================================================================================================================================================================


"""

This class helps "switch" windows by hiding windows and raising the desired window to the front (displaying it on the screen).

"""

class switchWindow(tk.Tk):
    # An init is required for every Python class.  The first argument taken is always self, which is used to refer to the individual instance's internal variables.
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set the desired size of our window for the interface.
        tk.Tk.geometry(self,"600x600")

        # The container is where we'll stack a bunch of frames on top of each other, then the one we want visible will be raised above the others.
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # This is the creation process for our frames.
        self.frames = {}

        # We put all of the pages in the same location, and the one on the top of the stacking order will be the one that is visible.
        for F in (mainMenu,createDeck,addCards,viewDecks,editDecks,deleteDecks):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # The first frame presented to the user is mainMenu, which is our program's main menu.  From here, they can nagivate to the other windows.
        self.show_frame(mainMenu)

    # This function is used to show the desired frame.  The title of the frame will change depending on which window the user clicks on.
    def show_frame(self, c):
        # Same functionality as above. It will move to the current from from the set of frames based on the choice.
        for F in (mainMenu,createDeck,addCards,viewDecks,editDecks,deleteDecks):
                frame = F(self.container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")

        # The frame title will change depending on the user's choice (where they click).
        if c == mainMenu:
            tk.Tk.wm_title(self,"Team Syntax Error's Project: Never Baguette")
        elif c == createDeck:
            tk.Tk.wm_title(self,"Create Deck")
        elif c == addCards:
            tk.Tk.wm_title(self,"Add Cards")
        elif c == viewDecks:
            tk.Tk.wm_title(self,"View Decks")
        elif c == editDecks:
            tk.Tk.wm_title(self,"Edit Decks")
        elif c == deleteDecks:
            tk.Tk.wm_title(self,"Delete Decks")
        else:
            tk.Tk.wm_title(self,"POTATOS")
        # Select the frame from the list depending on the user's input and raise it to the front.
        frame = self.frames[c]
        frame.tkraise()

    #Quit the program
    def quitProgram(self):
        tk.Tk.destroy(self)
#=========================================================================================================================================================================


"""

This class is used create and display the main menu.  It utilizes the switchWindow class to change the window to complete the function associated with the user's choice.
The widgets created inside are a part of each class pertaining to the GUI.  "Widgets" come in all shapes and sizes, and are customizable.  We mainly use buttons, but
other types also make an appearance.

"""

class mainMenu(tk.Frame):
    def __init__(self, master,controller):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.controller = controller

    def createWidgets(self):
        # Create a welcome message, which is the name of the program.
        welcomeMessage = tk.Message(self, text="\nNever Baguette\n\n", fg="darkgoldenrod", font="HeadLine 32 bold", width=500)
        welcomeMessage.pack(side="top")

        # Make a button for creating a new deck.  It has an associated command (function) which allows the user to create a new deck when the button is clicked.
        newCard = tk.Button(self, text="Create New Flashcard Deck!", font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1", command=self.create)
        newCard.pack(side="top")

        # Make a space between the newCard and viewCard Buttons
        spaceMessage1 = tk.Message(self, text="EmptyMessage", fg="white", font="Fireye 2")
        spaceMessage1.pack(side="top")

        # Make a button for viewing decks.  It has an associated command (function) which allows the user to view his/her decks when the button is clicked.
        viewCard = tk.Button(self, text="View Flashcard Deck!", font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1", command=self.view)
        viewCard.pack(side="top")

        # Make a space between the viewCard and editCard Buttons
        spaceMessage2 = tk.Message(self, text="EmptyMessage", fg="white", font="Fireye 2")
        spaceMessage2.pack(side="top")

        # Make a button for editing decks.  It has an associated command (function) which allows the user to edit his/her decks when the button is clicked.
        editCard = tk.Button(self, text="Edit Flashcard Deck!", font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1", command=self.edit)
        editCard.pack(side="top")

        # Make a space between the editCard and deleteCard Buttons
        spaceMessage3 = tk.Message(self, text="EmptyMessage", fg="white", font="Fireye 2")
        spaceMessage3.pack(side="top")

        # Make a button for deleting decks.  It has an associated command (function) which allows the user to delete his/her decks when the button is clicked.
        deleteCard = tk.Button(self, text="Delete Flashcard Deck!", font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1", command=self.delete)
        deleteCard.pack(side="top")

        quit = tk.Button(self, text="Quit Program", font='Fireye 16 bold', fg="red", activeforeground="red", command=self.quit)
        quit.pack(side="bottom")

    # All of the following functions simply move the program to the frame associated with the function called.
    def create(self):
        self.controller.show_frame(createDeck)
    def view(self):
        self.controller.show_frame(viewDecks)
    def edit(self):
        self.controller.show_frame(editDecks)
    def delete(self):
        self.controller.show_frame(deleteDecks)
    def quit(self):
        self.controller.quitProgram()
#=========================================================================================================================================================================


"""

This class is used create a new deck.  It displays a screen requiring the user to input:
    1) The deck's name
    2) The deck's description

Once these are entered, the program will create a new empty deck with that information.  It will then go straight to addCards, a class where the user adds cards to the
newly created deck.

"""

class createDeck(tk.Frame):
    def __init__(self, master,controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.createWidgets()

    def createWidgets(self):
        # Create variables for storing user's input for both deck name and deck description.
        self.deckName = StringVar()
        self.deckDescription = StringVar()

        # Make labels for "Enter Deck Name:" and "Enter Deck Description:"
        Label(self, text="\n\n\n\nEnter Deck Name:", font="HeadLine 16 bold", fg="darkgoldenrod").pack()
        self.deck_name_box = tk.Entry(self, textvariable=self.deckName, font="HeadLine 13 bold", fg="sienna4")
        self.deck_name_box.pack()

        Label(self, text="Enter Deck Description:", font="HeadLine 16 bold", fg="darkgoldenrod").pack()
        self.deck_desc_box = tk.Entry(self, textvariable=self.deckDescription, font="HeadLine 13 bold", fg="sienna4")
        self.deck_desc_box.pack()

        # Make a spacing between contents and button
        spaceMessage = tk.Message(self, text="EmptyMessage", fg="white", font="Fireye 2")
        spaceMessage.pack()

        # Make a button for saving a deck once content is read in from the user.
        save_button = Button(self, text="Save Deck", font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1", command=self.saveContents)
        save_button.pack()

        # Make a message to fill empty space down to the bottom of the page.
        empty_space = tk.Message(self)
        empty_space["text"] = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        empty_space.pack()

        # Make a button for returning to the main menu.
        main_menu_button = Button(self, text="Go back to Main Menu", font="Fireye 14 bold", fg="sienna4", activeforeground="LightSkyBlue1", command=self.goBack)
        main_menu_button.pack()

        # Make a button for quitting the program.
        exit_button = Button(self, text="Quit Program", font='Fireye 16 bold', fg="red", activeforeground="red", command=self.quit)
        exit_button.pack()

        # The status bar begins with a message to create a new deck
        self.status = Label(self,text="Create a New Deck",font="HeadLine 14 bold",fg="black",bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM,fill=X)

    # Save the deck into the mainController.
    def saveContents(self):
        global mainController
        global mainDeckName

        # Delete the previous status at the bottom of the screen. This will be recreated based on the conditionals below.
        self.status.destroy()

        # This will check if the user actually entered a deck name and description before it creates the new deck.  The first three cases handle both or either being empty.
        if len(self.deckName.get()) == 0 and len(self.deckDescription.get()) == 0:
            self.status = Label(self,text="Error: You need to enter a Deck Name and Description!",font="HeadLine 14 bold",fg="red",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        elif len(self.deckName.get()) == 0:
            self.status = Label(self,text="Error: You need to enter a Deck Name!",font="HeadLine 14 bold",fg="red",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        elif len(self.deckDescription.get()) == 0:
            self.status = Label(self,text="Error: You need to enter a Deck Description!",font="HeadLine 14 bold",fg="red",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        # If the user puts input in both boxes, the deck creation will be successful.
        else:
            mainDeckName = self.deckName.get()
            mainController.new_deck(self.deckName.get(),self.deckDescription.get())
            tkinter.messagebox.showinfo("New Deck Created!", "Successfully created Deck '" + self.deckName.get() + "'!")
            self.controller.show_frame(addCards)
            # Delete contents in entry fields to "reset" for the next time this function is called.
            self.deck_name_box.delete(0,END)
            self.deck_desc_box.delete(0,END)

    # The function called to return to the main menu.
    def goBack(self):
        self.controller.show_frame(mainMenu)
#=========================================================================================================================================================================


"""

This class is used to add cards to a newly created deck.  It displays a screen requiring the user to input:
    1) The card's term
    2) The card's definition

Once these are entered, the program will create a new card with that information in the previously created deck.  From here, the user can return to the main menu.
When they return to the main menu, the content of the mainController will be saved to the file.

"""

class addCards(tk.Frame):
    def __init__(self, master,controller):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.controller = controller

    def createWidgets(self):
        #  Create variables for storing user's input for both card front and card back.
        self.cardFront = StringVar()
        self.backCard = StringVar()

        # Make labels for "Enter Term:" and "Enter Flashcard Definition:"
        Label(self, text="\n\n\n\nEnter Flashcard Term:", font="HeadLine 16 bold", fg="darkgoldenrod").pack()
        self.card_term_box = tk.Entry(self, textvariable=self.cardFront, font="HeadLine 13 bold", fg="sienna4")
        self.card_term_box.pack()

        Label(self, text="Enter Flashcard Definition:", font="HeadLine 16 bold", fg="darkgoldenrod").pack()
        self.card_def_box = tk.Entry(self, textvariable=self.backCard, font="HeadLine 13 bold", fg="sienna4")
        self.card_def_box.pack()

        # Make a spacing between contents and button
        spaceMessage = tk.Message(self, text=" ", font="Fireye 2")
        spaceMessage.pack()

        # User needs to click save deck
        button = Button(self, text="Save Card", font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1", command=self.saveContents)
        button.pack()

        # Make a message to fill empty space down to the bottom of the page.
        empty_space = tk.Message(self)
        empty_space["text"] = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        empty_space.pack()

        # Make a button for returning to the main menu.
        main_menu_button = Button(self, text="Go back to Main Menu", font="Fireye 14 bold", fg="sienna4", activeforeground="LightSkyBlue1", command=self.goBack)
        main_menu_button.pack()

        # Make a button for quitting the program.
        exit_button = Button(self, text="Quit Program", font='Fireye 16 bold', fg="red", activeforeground="red", command=self.quit)
        exit_button.pack()

        # The status bar begins with a message to add cards to the new deck.
        message_text = "Add Flashcards to Deck '" + mainDeckName + "'."
        self.status = Label(self,text=message_text,font="HeadLine 14 bold",fg="black",bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM,fill=X)

    #  Save the new cards into the mainController.
    def saveContents(self):
        global mainController
        global mainDeckName
        global mainFileSys

        # Delete the previous status at the bottom of the screen. This will be recreated based on the conditionals below.
        self.status.destroy()

        # This will check if the user actually entered a term and definition before it creates the new card.  The first three cases handle both or either being empty.
        if len(self.cardFront.get()) == 0 and len(self.backCard.get()) == 0:
            self.status = Label(self,text="Error: You need to enter a Term and Definition.",font="HeadLine 14 bold",fg="red",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        elif len(self.cardFront.get()) == 0:
            self.status = Label(self,text="Error: You need to enter a Term.",font="HeadLine 14 bold",fg="red",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        elif len(self.backCard.get()) == 0:
            self.status = Label(self,text="Error: You need to enter a Definition.",font="HeadLine 14 bold",fg="red",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        # If the user puts input in both boxes, the deck creation will be successful.
        else:
            deck = mainController.get_deck(mainDeckName)
            deck.add_card(self.cardFront.get(), self.backCard.get())
            # Delete contents in entry fields to "reset" for the next time this function is called.
            self.card_term_box.delete(0,END)
            self.card_def_box.delete(0,END)
            card_text = "Flashcard successfully added to Deck '" + mainDeckName + "'."
            self.status = Label(self,text=card_text,font="HeadLine 14 bold",fg="lime green",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)

    # The function called to return to the main menu.
    def goBack(self):
        mainFileSys.write_to_file(mainController)
        # This will save the deck name if the user just chooses to go back to the main menu.
        self.controller.show_frame(mainMenu)

    #Quit the program and save the contents to the file.
    def quit(self):
        mainFileSys.write_to_file(mainController)
        self.controller.quitProgram()
#=========================================================================================================================================================================


"""

This class is used to view the cards in the decks the user has created.  They select a deck by clicking a button associated with the deck, and the first card's term will
be displayed.  They can click "Flip" to switch between which side of the card is being shown. Clicking "Next Card" or "Previous Card" allows them to switch between cards.

"""

class viewDecks(tk.Frame):
    def __init__(self, master,controller):
        item = tk.Frame.__init__(self, master)
        self.controller = controller
        self.createWidgets()
        # Because of the way replacing buttons is implemented in tkinter, we need to have private members created for each button that may be replaced.
        self.welcomeMessage = tk.Message(self)
        self.currentDeck = tk.Message(self)
        self.emptyDeck = tk.Message(self)
        self.termGUI = tk.Message(self)
        self.defGUI = tk.Message(self)
        self.answer = tk.Button(self, text="Flip", font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1")
        self.previousCard = tk.Button(self, text="Previous Card", font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1")
        self.nextCard = tk.Button(self, text="Next Card", font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1")

    def createWidgets(self):
        self.index = 0

        # Make a message to ask the user which deck they wish to work with.
        welcomeMessage = tk.Message(self, text="\nWhich Deck to View\n", font="HeadLine 16 bold", fg="darkgoldenrod", width=1000)
        welcomeMessage.pack(side = "top")

        # Get all the decks from the mainController.  They will be needed to make the buttons for each deck.
        decks = mainController.get_decks()

        # If there are no decks, no buttons will be created for viewing the decks. A message will be displayed to inform the user.
        if not decks:
            no_decks = tk.Message(self, text="\nThere are no decks to view!\n", font="HeadLine 14 bold", fg="darkgoldenrod", width=1000)
            no_decks.pack(side = "top")
        # Create a button for each individual deck in the mainController.
        else:
            for deck in decks:
                deck_name = deck.get_name()
                self.deck = tk.Button(self, text=deck_name, font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1")
                # A lambda function is made so that each deck's function is associated with only itself.
                self.deck["command"] = lambda nameOfDeck = deck_name: self.view(nameOfDeck)
                self.deck.pack(side="top")

        # Make a button for quitting the program.
        exit_button = Button(self, text="Quit Program", font='Fireye 16 bold', fg="red", activeforeground="red", command=self.quit)
        exit_button.pack(side = "bottom")

        # Make a button for returning to the main menu.
        main_menu_button = Button(self, text="Go back to Main Menu", font="Fireye 14 bold", fg="sienna4", activeforeground="LightSkyBlue1", command=self.goBack)
        main_menu_button.pack(side = "bottom")

    # This function displays the deck being viewed and the current card.  It also creates the buttons for flipping and going to the next and previous cards.
    def view(self, deck_name):
        # Hide the previous buttons so they may be recreated.
        self.termGUI.pack_forget()
        self.defGUI.pack_forget()
        self.answer.pack_forget()
        self.previousCard.pack_forget()
        self.nextCard.pack_forget()
        self.emptyDeck.pack_forget()
        self.currentDeck.pack_forget()

        # Get the deck.
        deck = mainController.get_deck(deck_name)

        # Create lists to store the terms and definitions of the cards in the deck.
        self.termList = []
        self.definitionList = []
        self.index = 0

        cards = deck.get_cards()
        for card in cards:
            self.termList.append(card.get_term())
            self.definitionList.append(card.get_definition())

        # Check to see if there are any cards in the deck.
        if(len(self.termList) == 0):
            self.emptyDeck = tk.Message(self)
            self.emptyDeck["font"] = "HeadLine 14 bold"
            self.emptyDeck["fg"] = "darkgoldenrod"
            self.emptyDeck["text"] = "\nDeck '" + deck_name + "' is empty.\n"
            self.emptyDeck["width"] = 1000
            self.emptyDeck.pack(side = "top")
        # If there are cards, we will create the buttons.
        else:
            self.currentDeck["text"] = "\nNow Viewing Deck '" + deck_name + "'\n"
            self.currentDeck["width"] = 1000
            self.currentDeck["font"] = "HeadLine 14 bold"
            self.currentDeck["fg"] = "darkgoldenrod"
            self.currentDeck.pack(side = "top")

            self.termGUI["font"] = "Fireye 14 bold"
            self.termGUI["fg"] = 'orange red'
            self.termGUI["width"] = 600
            self.termGUI["text"] = self.termList[self.index] + "\n"
            self.termGUI.pack(side = "top")

            self.defGUI["font"] = "Fireye 14 bold"
            self.defGUI["fg"] = 'white'
            self.defGUI["width"] = 600
            self.defGUI["text"] = self.definitionList[self.index] + "\n"
            self.defGUI.pack(side = "top")

            self.answer["command"] = lambda: self.openFrame()
            self.answer.pack(side = "top")

            self.previousCard["command"] = lambda : self.decrementIndex()
            self.previousCard.pack(side = "left")

            self.nextCard["command"] = lambda : self.incrementIndex()
            self.nextCard.pack(side = "right")

    # Increment the index. It checks the boundary of the list and changes the card on the screen to the next card if possible.
    def incrementIndex(self):
        self.index += 1

        if (self.index == len(self.termList)):
            self.index = len(self.termList) - 1
        else:
            self.termGUI["text"] = self.termList[self.index] + "\n"
            self.termGUI.pack(side = "top")

            self.defGUI["text"] = self.definitionList[self.index] + "\n"
            self.defGUI.pack(side = "top")

    # Decrement the index. It checks the boundary of the list and changes the card on the screen to the previous card if possible.
    def decrementIndex(self):
        if (self.index == 0):
            self.index = 0
        else:
            self.index -= 1
            self.termGUI["text"] = self.termList[self.index] + "\n"
            self.termGUI.pack(side = "top")

            self.defGUI["text"] = self.definitionList[self.index] + "\n"
            self.defGUI.pack(side = "top")

    # Swaps between revealing and hiding the text based on the user clicking "Flip".
    def openFrame(self):
        if self.defGUI["fg"] == 'white':
            self.defGUI["fg"] = 'orange red'
        elif self.defGUI["fg"] == 'orange red':
            self.defGUI["fg"] = 'white'

        if self.termGUI["fg"] == 'orange red':
            self.termGUI["fg"] = 'white'
        elif self.termGUI["fg"] == 'white':
            self.termGUI["fg"] = 'orange red'

    # The function called to return to the main menu.
    def goBack(self):

        self.controller.show_frame(mainMenu)
#=========================================================================================================================================================================


"""

This class is used to edit the cards in the decks the user has created.  The user selects a deck by clicking a button associated with the deck, and the first card's term
and definition will be displayed.  Their options are to "Add New Card" to the deck, "Edit Card" to modify the current entry, or "Delete Card" to remove the current card
from the deck.

"""

class editDecks(tk.Frame):
    def __init__(self, master,controller):
        item = tk.Frame.__init__(self, master)
        self.controller = controller
        self.createWidgets()
        # Because of the way replacing buttons is implemented in tkinter, we need to have private members created for each button that may be replaced.
        self.currentDeck = tk.Message(self, font="HeadLine 14 bold", fg="darkgoldenrod")
        self.emptyDeck = tk.Message(self)
        self.termGUI = tk.Message(self, font="Fireye 14 bold", fg="black", width=700)
        self.defGUI = tk.Message(self, font="Fireye 14 bold", fg="black", width=700)
        self.addCard = tk.Button(self, text="Add New Card", font="Fireye 16 bold", fg="orange red", activeforeground="LightSkyBlue1")
        self.editCard = tk.Button(self, text="Edit Card", font="Fireye 16 bold", fg="orange red", activeforeground="LightSkyBlue1")
        self.deleteCard = tk.Button(self, text="Delete Card", font="Fireye 16 bold", fg="orange red", activeforeground="LightSkyBlue1")
        self.previousCard = tk.Button(self, text="Previous Card", font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1")
        self.nextCard = tk.Button(self, text="Next Card", font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1")
        self.cardFront = StringVar()
        self.backCard = StringVar()
        self.card_term_label = Label(self, text="Enter Flashcard Term:", font="HeadLine 16 bold", fg="darkgoldenrod")
        self.card_def_label = Label(self, text="Enter Flashcard Definition:", font="HeadLine 16 bold", fg="darkgoldenrod")
        self.card_term_box = tk.Entry(self, textvariable=self.cardFront, font="HeadLine 13 bold", fg="sienna4")
        self.card_def_box = tk.Entry(self, textvariable=self.backCard, font="HeadLine 13 bold", fg="sienna4")
        self.spaceMessage = tk.Message(self, text=" ", fg="white", font="Fireye 2")
        self.save_button = tk.Button(self, text="Save Card", font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1")
        self.cancel_button = tk.Button(self, text="Cancel Card Creation", font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1")

    def createWidgets(self):
        self.index = 0

        # Make a message to ask the user which deck they wish to work with.
        welcomeMessage = tk.Message(self, text="\nWhich Deck to Edit\n", font="HeadLine 16 bold", fg="darkgoldenrod", width=1000)
        welcomeMessage.pack(side = "top")

        # Get all the decks from the mainController.  They will be needed to make the buttons for each deck.
        decks = mainController.get_decks()

        # If there are no decks, no buttons will be created for editing the decks. A message will be displayed to inform the user.
        if not decks:
            no_decks = tk.Message(self, text="\nThere are no decks to edit!\n", font="HeadLine 14 bold", fg="darkgoldenrod", width=1000)
            no_decks.pack(side = "top")
        # Create a button for each individual deck in the mainController.
        else:
            for deck in decks:
                deck_name = deck.get_name()
                self.deck = tk.Button(self, text=deck_name, font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1")
                # A lambda function is made so that each deck's function is associated with only itself.
                self.deck["command"] = lambda nameOfDeck = deck_name: self.edit(nameOfDeck)
                self.deck.pack(side="top")

        # Make a button for quitting the program.
        exit_button = Button(self, text="Quit Program", font='Fireye 16 bold', fg="red", activeforeground="red", command=self.quit)
        exit_button.pack(side = "bottom")

        # Make a button for returning to the main menu.
        main_menu_button = Button(self, text="Go back to Main Menu", font="Fireye 14 bold", fg="sienna4", activeforeground="LightSkyBlue1", command=self.goBack)
        main_menu_button.pack(side = "bottom")

        self.status = Label(self,text="",bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM,fill=X)

    # This function displays the currently selected deck for editing and the current card.  It also creates the buttons for adding, editing, and deleting.
    def edit(self, deck_name):
        # Hide the previous buttons so they may be recreated.
        self.currentDeck.pack_forget()
        self.termGUI.pack_forget()
        self.defGUI.pack_forget()
        self.previousCard.pack_forget()
        self.nextCard.pack_forget()
        self.addCard.pack_forget()
        self.editCard.pack_forget()
        self.deleteCard.pack_forget()
        self.emptyDeck.pack_forget()
        self.status.destroy()
        self.card_term_box.pack_forget()
        self.card_def_box.pack_forget()
        self.card_term_label.pack_forget()
        self.card_def_label.pack_forget()
        self.spaceMessage.pack_forget()
        self.save_button.pack_forget()
        self.cancel_button.pack_forget()


        # Get the deck.
        deck = mainController.get_deck(deck_name)

        # Create lists to store the terms and definitions of the cards in the deck.
        self.termList = []
        self.definitionList = []
        self.index = 0

        cards = deck.get_cards()
        for card in cards:
            self.termList.append(card.get_term())
            self.definitionList.append(card.get_definition())

        # Check to see if there are any cards in the deck.
        if(len(self.termList) == 0):
            self.emptyDeck = tk.Message(self, text="\nDeck is Empty!\n", font="HeadLine 14 bold", fg="darkgoldenrod", width=1000)
            self.emptyDeck.pack(side = "top")

            self.addCard["command"] = lambda: self.add_card(deck_name)
            self.addCard.pack(side = "top")
        # If there are cards, we will create the buttons.
        else:
            # Shows information about the current deck and the current card's term and definition.
            self.currentDeck["text"] = "\nNow Editing Deck " + deck_name + "\n"
            self.currentDeck["width"] = 1000
            self.currentDeck.pack(side = "top")

            self.termGUI["text"] = self.termList[self.index] + "\n"
            self.termGUI.pack(side = "top")

            self.defGUI["width"] = 600
            self.defGUI["text"] = self.definitionList[self.index] + "\n"
            self.defGUI.pack(side = "top")

            # The functions below are for modifying the current card in the deck. Each one has a function associated with it.
            self.addCard["command"] = lambda: self.add_card(deck_name)
            self.addCard.pack(side = "top")

            self.editCard["command"] = lambda: self.edit_card(deck_name)


            self.deleteCard["command"] = lambda: self.delete_card(deck_name)
            self.deleteCard.pack(side = "top")

            self.previousCard["command"] = lambda : self.decrementIndex()
            self.previousCard.pack(side = "left")

            self.nextCard["command"] = lambda : self.incrementIndex()
            self.nextCard.pack(side = "right")

    # Increment the index. It checks the boundary of the list and changes the card on the screen to the next card if possible.
    def incrementIndex(self):
        self.index += 1

        if (self.index == len(self.termList)):
            self.index = len(self.termList) - 1
        else:
            self.termGUI["text"] = self.termList[self.index] + "\n"
            self.termGUI.pack(side = "top")

            self.defGUI["text"] = self.definitionList[self.index] + "\n"
            self.defGUI.pack(side = "top")

    # Decrement the index. It checks the boundary of the list and changes the card on the screen to the previous card if possible.
    def decrementIndex(self):

        if (self.index == 0):
            self.index = 0
        else:
            self.index -= 1
            self.termGUI["text"] = self.termList[self.index] + "\n"
            self.termGUI.pack(side = "top")

            self.defGUI["text"] = self.definitionList[self.index] + "\n"
            self.defGUI.pack(side = "top")

    # For adding an individual card to the currently selected deck.
    def add_card(self, deck_name):
        self.addCard.pack_forget()
        self.deleteCard.pack_forget()
        self.status.destroy()

        self.card_term_label.pack()
        self.card_term_box.pack()
        self.card_def_label.pack()
        self.card_def_box.pack()
        # Make a spacing between contents and button
        self.spaceMessage.pack()

        # User needs to click save deck.
        self.save_button["command"] = lambda: self.save_card(deck_name)
        self.save_button.pack()

        # To stop the action.
        self.cancel_button["command"] = lambda: self.cancel_new_card()
        self.cancel_button.pack()

        # The status bar begins with a message to add cards to the new deck.
        message_text = "Add Flashcards to Deck '" + deck_name + "'."
        self.status = Label(self,text=message_text,font="HeadLine 14 bold",fg="black",bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM,fill=X)

    # For saving a new card to the deck.
    def save_card(self, deck_name):
        global mainController
        global mainDeckName
        global mainFileSys

        # Delete the previous status at the bottom of the screen. This will be recreated based on the conditionals below.
        self.status.destroy()

        # This will check if the user actually entered a term and definition before it creates the new card.  The first three cases handle both or either being empty.
        if len(self.cardFront.get()) == 0 and len(self.backCard.get()) == 0:
            self.status = Label(self,text="Error: You need to enter a Term and Definition.",font="HeadLine 14 bold",fg="red",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        elif len(self.cardFront.get()) == 0:
            self.status = Label(self,text="Error: You need to enter a Term.",font="HeadLine 14 bold",fg="red",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        elif len(self.backCard.get()) == 0:
            self.status = Label(self,text="Error: You need to enter a Definition.",font="HeadLine 14 bold",fg="red",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        # If the user puts input in both boxes, the card creation will be successful.
        else:
            for deck in mainController.get_decks():
                if deck.get_name() == deck_name:
                    deck.add_card(self.cardFront.get(), self.backCard.get())

            mainFileSys.write_to_file(mainController)
            # Delete contents in entry fields to "reset" for the next time this function is called.
            self.card_term_box.delete(0,END)
            self.card_def_box.delete(0,END)
            card_text = "Flashcard successfully added to Deck '" + deck_name + "'."
            self.status = Label(self,text=card_text,bd=1,font="HeadLine 14 bold",fg="lime green",relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
            self.refresh_buttons()
            return

    def cancel_new_card(self):
        self.refresh_buttons()
        self.status.destroy()
        self.status = Label(self,text="Cancelled.",bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM,fill=X)
        return

    def refresh_buttons(self):
        self.card_term_box.pack_forget()
        self.card_def_box.pack_forget()
        self.card_term_label.pack_forget()
        self.card_def_label.pack_forget()
        self.spaceMessage.pack_forget()
        self.save_button.pack_forget()
        self.cancel_button.pack_forget()
        self.addCard.pack_forget()
        self.addCard.pack(side = "top")
        self.deleteCard.pack(side="top")

    # The function for deleting the card selected by the user.
    def delete_card(self, deck_name):
        global mainController
        global deckName
        global mainFileSys

        # Check if the user really wants to delete the card.
        dialog_title = 'Deletion Confirmation'
        dialog_text = 'Are you sure you want to delete this card?'
        answer = tkinter.messagebox.askquestion(dialog_title, dialog_text)

        if answer == 'yes':
            deck = mainController.get_deck(deck_name)
            for card in deck.get_cards():
                # When we match the card, then we will remove that card from the deck.
                if card.get_term() == self.termList[self.index]:
                    if (self.index == len(self.termList)-1):
                        self.termList.remove(self.termList[self.index])
                        self.definitionList.remove(self.definitionList[self.index])
                        self.index = self.index - 1
                    else:
                        self.termList.remove(self.termList[self.index])
                        self.definitionList.remove(self.definitionList[self.index])
                    deck.remove_card(card.get_term())

            # Change the term and definition displayed to reflect the list with the newly deleted card.  That card's information will no longer show.
            if len(self.termList) >= 0:
                self.termGUI["text"] = self.termList[self.index] + "\n"
                self.defGUI["text"] = self.definitionList[self.index] + "\n"
            else:
                self.index = 0
                self.termGUI["text"] = "\n"
                self.defGUI["text"] = "\n"
                self.emptyDeck.pack(side = "top")

            # Save the changes to the file system.
            mainFileSys.write_to_file(mainController)

        else:
            pass


    #TODO make it possible to edit cards
    def edit_card(self, deck_name):
        # this will reformat the GUI with textboxes
        self.cardFront = self.termList[self.index]
        self.backCard = self.definitionList[self.index]

        self.previousCard.pack_forget()
        self.nextCard.pack_forget()
        self.editCard.pack_forget()
        self.addCard.pack_forget()
        self.deleteCard.pack_forget()
        self.termGUI.pack_forget()
        self.defGUI.pack_forget()

        self.card_term_box.insert(END, self.cardFront)
        self.card_term_box.pack()

        self.card_def_box.insert(END, self.backCard)
        self.card_def_box.pack()

        # User needs to click to update card
        self.button["command"] = lambda : self.save_card_edit(deck_name, self.cardFront, self.backCard)
        self.button.pack(side="top")

        # To
        self.cancel_button["command"] = lambda: self.cancel_edit_card()
        self.cancel_button.pack()

        # The status bar begins with a message to add cards to the new deck.
        message_text = "Editing Flashcard from Deck '" + deck_name + "'."
        self.status = Label(self,text=message_text,bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM,fill=X)

    def save_card_edit(self, deck_name, cardFront, backCard):
        global mainController
        global mainDeckName
        global mainFileSys

        self.status.destroy()

        # This will check if the user actually has a term and definition before it edits the new card.  The first three cases handle both or either being empty.
        if len(self.cardFront.get()) == 0 and len(self.backCard.get()) == 0:
            self.status = Label(self,text="Error: You need to enter a Term and Definition.",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        elif len(self.cardFront.get()) == 0:
            self.status = Label(self,text="Error: You need to enter a Term.",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        elif len(self.backCard.get()) == 0:
            self.status = Label(self,text="Error: You need to enter a Definition.",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
        # If the user puts input in both boxes, the deck creation will be successful.
        else:
            for deck in mainController.get_decks():
                if deck.get_name() == deck_name:
                    deck.edit_card(self.index, cardFront, backCard)


            mainFileSys.write_to_file(mainController)

            current_deck = mainController.get_deck(deck_name).get_cards()
            for card in current_deck:
                if card.get_term() == cardFront:
                    self.termList[self.index] = card.get_term()
                    self.definitionList[self.index] = card.get_definition()

        self.card_term_box.delete(0,END)
        self.card_def_box.delete(0,END)

        self.card_term_box.pack_forget()
        self.card_def_box.pack_forget()
        self.button.pack_forget()

        self.termGUI["text"] = self.termList[self.index] + "\n"
        self.termGUI.pack(side = "top")

        self.defGUI["text"] = self.definitionList[self.index] + "\n"
        self.defGUI.pack(side = "top")

        self.addCard.pack(side = "top")
        self.editCard.pack(side = "top")
        self.deleteCard.pack(side = "top")
        self.previousCard.pack(side = "left")
        self.nextCard.pack(side = "right")

        def cancel_new_card(self):
            self.status.destroy()
            self.status = Label(self,text="Cancelled.",bd=1,relief=SUNKEN,anchor=W)
            self.status.pack(side=BOTTOM,fill=X)
            self.addCard.pack(side = "top")
            self.editCard.pack(side = "top")
            self.deleteCard.pack(side = "top")
            self.previousCard.pack(side = "left")
            self.nextCard.pack(side = "right")
            return

    # The function called to return to the main menu.
    def goBack(self):
            self.controller.show_frame(mainMenu)

#=========================================================================================================================================================================


"""

This class is used to delete entire decks.  The user selects a deck by clicking a button associated with the deck, and then they will be asked to confirm the deletion.
If "yes", the deck will be removed from the mainController and the mainFileSys will be updated to reflect the change.

"""

class deleteDecks(tk.Frame):
    def __init__(self, master,controller):
        item = tk.Frame.__init__(self, master)
        self.controller = controller
        self.createWidgets()
        # We need private variables for the choice in deletion and for the deck list index to be kept track of.
        self.choice = tk.Message(self, font="HeadLine 14 bold", fg="darkgoldenrod", width=1000)
        self.deckList = []

    def createWidgets(self):
        global mainController
        global mainFileSys

        # Make a message to ask the user which deck they wish to work with.
        welcomeMessage = tk.Message(self, font="HeadLine 16 bold", fg="darkgoldenrod")
        welcomeMessage["text"] = "\nWhich Deck to Delete?\n"
        welcomeMessage["width"] = 1000
        welcomeMessage.pack(side = "top")

        # Get all the decks from the mainController.  They will be needed to make the buttons for each deck.
        decks = mainController.get_decks()
        self.deckList = decks

        # If there are no decks, no buttons will be created for deleting the decks. A message will be displayed to inform the user.
        if not decks:
            no_decks = tk.Message(self, text="\nThere are no decks to delete!\n", font="HeadLine 16 bold", fg="darkgoldenrod", width=1000)
            no_decks.pack(side = "top")

        # If the else is reached, then we have decks.
        # Create a button for each individual deck in the mainController.
        else:
            for deck in decks:
                deck_name = deck.get_name()
                self.deck = tk.Button(self, text=deck_name, font="Fireye 16 bold", fg="sienna4", activeforeground="LightSkyBlue1")
                # A lambda function is made so that each deck's function is associated with only itself.
                self.deck["command"] = lambda nameOfDeck = deck_name: self.delete(nameOfDeck)
                self.deck.pack(side="top")

        # Make a button for quitting the program.
        exit_button = Button(self, text="Quit Program", font='Fireye 16 bold', fg="red", activeforeground="red", command=self.quit)
        exit_button.pack(side = "bottom")

        # Make a button for returning to the main menu.
        main_menu_button = Button(self, text="Go back to Main Menu", font="Fireye 14 bold", fg="sienna4", activeforeground="LightSkyBlue1", command=self.goBack)
        main_menu_button.pack(side = "bottom")

    # This function prompts the user to confirm the deletion. If they confirm, then the deck is deleted.
    def delete(self, deck_name):
        # Hide whatever the previous choice message.
        self.choice.pack_forget()

        # Check if the user really wants to delete the card.
        dialog_title = 'Deletion Confirmation'
        dialog_text = 'Are you sure you want to delete this deck?'
        answer = tkinter.messagebox.askquestion(dialog_title, dialog_text)

        if answer == 'yes':
            # Check if the user has already deleted that deck in the current "Delete Decks" window
            if not mainController.get_deck(deck_name):
                self.choice["text"] = "\nDeck '" + deck_name + "' was already deleted.\n\n\n"
            # This is the case where the deck has been selected to be deleted for the first time.
            else:
                mainController.delete_deck(deck_name)
                mainFileSys.write_to_file(mainController)
                self.choice["text"] = "\nSuccessfully deleted: '" + deck_name + "'.\n\n\n"
        else:
            self.choice["text"] = "\nDeck '" + deck_name + "' has not been deleted.\n\n\n"

        # The user's choice will be displayed at the bottom of the screen.
        self.choice.pack(side = "bottom")

    # The function called to return to the main menu.
    def goBack(self):
        self.controller.show_frame(mainMenu)

#=======1=========2=========3=========4=========5=========6=========7=========8=========9=========0=========1=========2=========3=========4=========5=========6========7**
