import tkinter as Tk
 
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
        
        self.index = 0
        self.questionString = "What color is the sky?", "what is 3+5?", "What is blue?", "What are pants?"
        #print (questionString)

        self.answerString = "Blue", "8", "A Color", "For your legs"
        #print (answerString)
        
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
