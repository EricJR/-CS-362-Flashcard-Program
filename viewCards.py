import tkinter as Tk
import re
import sys
import os

# Testing to make it work in Terminal.
class Flashcard:
    def __init__ (self, term, definition):
        self._term = term
        self._definition = definition
    
    def get_term(self):
        return self._term
        
    def get_definition(self):
        return self._definition
        
    def set_term(self, user_term):
        self._term = user_term
        
    def set_definition(self, user_definition):
        self._definition = user_definition
        
    def __str__(self):
        return ("\tQ: %s \n\tA: %s" % (self._term, self._definition))
    
class Deck:
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._cards = []
        
    def get_name(self):
        return self._name
    
    def get_description(self):
        return self._description
        
    def get_cards(self):
        return self._cards
        
    def add_card(self, term, definition):
        new_card = Flashcard(term, definition)
        self._cards.append(new_card)

    def __str__(self):
        return ("%s" % (self._name))
        
class FlashcardController:
    def __init__(self):
        self._decks = []
        
    def get_decks(self):
        return self._decks

    def get_deck(self, name):
        for deck in self._decks:
            if deck.get_name() == name:
                return deck
        return

    def new_deck(self, deckname, deckDescription):
        newDeck = Deck(deckname, deckDescription)
        self._decks.append(newDeck)
    
    def add_cards_to_deck(self, name):
        test_decks = self._decks
        add_cards_choice = "Y"
        
        for deck in test_decks:
            if deck.get_name() == name:
                while add_cards_choice != "N":
                    new_term = input("Enter card term: ")
                    new_definition = input("Enter card definition: ")
                    deck.add_card(new_term, new_definition)
                    add_cards_choice = input("Add more cards? (Y/N): ")
                #for card in deck.get_cards():
                #    print("Added card:\n",card)
                
    def __str__(self):
        #to_print = ""
        #for deck in self._decks:
        #    to_print += str(deck) + ", "
         
        #return ("%s" % (to_print[:-2]))
        
        # Convert the Deck objects in the decks[] list to str, and modify the string
        # with a comma between each object for easier reading.
        return (", ".join(map(str, self._decks)))









class FileSystemStorage:
    def __init__(self):
        self.file_name = "flashcards_file.txt"

        #filepath = os.path.join("/library",self.file_name)

        #subdir = os.path.join("/library/" + self.file_name)

        #try:
        #    os.mkdir(subdir)
        #except:
        #    print("failed")

        # Try to open the file. If it does not exist (first user run), it will be created. Otherwise, it confirms success.
        with open(self.file_name,"a+") as f:
            pass


    def get_file_name(self):
        return self.file_name

    def read_from_file(self, ctrler):
        infile = self.file_name
        file_lines = []
        RE_lines = []
        
        with open(infile, "r") as ifh:
            for line in ifh:
                file_lines.append(line)
                
        pattern = re.compile(r"@@@|~~")
        
        for line in file_lines:
            RE_lines.append(pattern.split(line))
            
        for line in RE_lines:
            if line[0] == '':
                try:
                    deck_name = line[1]
                    deck_desc = line[2].replace('\n','')
                    ctrler.new_deck(deck_name, deck_desc)
                except:
                    card_term = line[0]
                    card_def = line[1].replace('\n','')
                    ctrler.get_deck(deck_name).add_card(card_term, card_def)
                    #print ("\tCard term: {}\n\tCard definition: {}".format(card_term, card_def))
            else:
                card_term = line[0]
                card_def = line[1].replace('\n','')
                ctrler.get_deck(deck_name).add_card(card_term, card_def)
                #print ("\tCard term: {}\n\tCard definition: {}".format(card_term, card_def))

        return ctrler

    def write_to_file(self, ctrler):
        outfile = self.file_name
        #outfile = os.path.abspath("library/" + self.file_name)
      
        with open(outfile, "w") as f:
            for deck in ctrler.get_decks():
                deck_print = "@@@" + deck.get_name() + "~~" + deck.get_description() + "\n"
                f.write(deck_print)
                for card in deck.get_cards():
                    card_print = card.get_term() + "~~" + card.get_definition() + "\n"
                    f.write(card_print)


 
########################################################################
class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        
        self.root = parent
        self.root.title("Main frame")
        self.frame = Tk.Frame(parent)
        self.frame.pack()
        
        
        self.questionString = []
        self.answerString = [] 
        self.index = 0
        
        controller = FlashcardController()
        file_sys = FileSystemStorage()
        debug = True
    
        # Testing the file system
        file_sys.read_from_file(controller)
        
        decks = controller.get_decks()
        for deck in decks:
            cards = deck.get_cards()
            for card in cards:
                self.questionString.append(card.get_term())
                self.answerString.append(card.get_definition())
        
        print("Length qstring = ", len(self.questionString))
        
        # self.questionString = "What color is the sky?", "what is 3+5?", "What is blue?", "What are pants?"
 #        #print (questionString)
 #
 #        self.answerString = "Blue", "8", "A Color", "For your legs"
 #        #print (answerString)
        
        hi_there = Tk.Message(self.frame)
        hi_there["text"] = "\nNow Viewing Deck!\n"
        hi_there.pack(side = "top")

        self.questionGUI = Tk.Message(self.frame)
        self.questionGUI["fg"] = 'black'
        self.questionGUI["text"] = self.questionString[self.index] + "\n"
        self.questionGUI.pack(side = "top")

        self.answerGUI = Tk.Message(self.frame)
        self.answerGUI["fg"] = 'white'  
        self.answerGUI["text"] = self.answerString[self.index] + "\n"
        self.answerGUI.pack(side = "top")



        # answer = Tk.Button(self.frame, text="Show Answer", command=self.openFrame(answerGUI))
    #         answer.pack(side = "top")


        answer = Tk.Button(self.frame, text="Flip")
        answer["command"] = lambda: self.openFrame()
        answer.pack(side = "top")

        # if answer:
    #             self.openFrame(answerGUI)

        previousCard = Tk.Button(self.frame, text="Previous Card")
        previousCard["command"] = lambda : self.decrementIndex()
        previousCard.pack(side = "left")

        nextCard = Tk.Button(self.frame, text="Next Card")
        nextCard["command"] = lambda : self.incrementIndex()
        nextCard.pack(side = "right")
        
        

        quit = Tk.Button(self.frame, text="Quit Program", command=root.destroy)
        quit.pack(side = "bottom")

        menu = Tk.Button(self.frame, text="Back to Menu")
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
 
    #----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()
 
    #----------------------------------------------------------------------
    
    def say_hi(self):
        print("Welcome to the flash card program!")
        say_hi.pack()
    
    # def answerGUI(self, answerString):
   #      print ("answerGUI")
    
    def openFrame(self):
        # self.hide()
#         otherFrame = Tk.Toplevel()
#         otherFrame.geometry("500x500")
#         otherFrame.title("Answer")
        
        if self.answerGUI["fg"] == 'white':
            self.answerGUI["fg"] = 'black'
        elif self.answerGUI["fg"] == 'black':
            self.answerGUI["fg"] = 'white'
            
        if self.questionGUI["fg"] == 'black':
            self.questionGUI["fg"] = 'white'
        elif self.questionGUI["fg"] == 'white':
            self.questionGUI["fg"] = 'black'
        
        #answerGUI["fg"] = 'black'
        # answerGUI.pack()
#         questionGUI.pack()
        
        # print (questionString)
        
        # answerGUI = Tk.Message(self.frame)
#         answerGUI["fg"] = 'white'
#         answerGUI["text"] = "\nAnswer:\n" + answerString
#         answerGUI.pack(side = "top")
        
        # answer = Tk.Button(otherFrame, text="Close", command=handler)
#         answer.pack(side = "bottom")
        
    def previousCards(self):
        previousCard.pack()
        
    def menu(self):
        menu.pack()
        
    def quit(self):
        quit.pack()
        
    #----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        otherFrame.destroy()
        self.show()
 
    #----------------------------------------------------------------------
    def show(self):
        self.root.update()
        self.root.deiconify()

#----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("500x500")
    app = MyApp(root)
    root.mainloop()
