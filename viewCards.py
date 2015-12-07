import tkinter as Tk
import re
import sys
import os
from flashcard_classes import *

########################################################################
class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        
        self.root = parent
        self.root.title("View cards frame")
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

        hi_there = Tk.Message(self.frame)
        hi_there["text"] = "\nNow Viewing Deck!\n"
        hi_there["width"] = 1000
        hi_there.pack(side = "top")

        self.questionGUI = Tk.Message(self.frame)
        self.questionGUI["fg"] = 'black'
        self.questionGUI["width"] = 600
        self.questionGUI["text"] = self.questionString[self.index] + "\n"
        self.questionGUI.pack(side = "top")

        self.answerGUI = Tk.Message(self.frame)
        self.answerGUI["fg"] = 'white'  
        self.answerGUI["width"] = 600
        self.answerGUI["text"] = self.answerString[self.index] + "\n"
        self.answerGUI.pack(side = "top")

        answer = Tk.Button(self.frame, text="Flip")
        answer["command"] = lambda: self.openFrame()
        answer.pack(side = "top")
        
        

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
    
    def openFrame(self):
        if self.answerGUI["fg"] == 'white':
            self.answerGUI["fg"] = 'black'
        elif self.answerGUI["fg"] == 'black':
            self.answerGUI["fg"] = 'white'
            
        if self.questionGUI["fg"] == 'black':
            self.questionGUI["fg"] = 'white'
        elif self.questionGUI["fg"] == 'white':
            self.questionGUI["fg"] = 'black'
        
    #----------------------------------------------------------------------

#----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("700x500")
    app = MyApp(root)
    root.mainloop()
