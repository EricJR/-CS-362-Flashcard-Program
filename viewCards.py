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
        
        questionString = "What color is the sky?"
        print (questionString)
        
        answerString = "Blue"
        print (answerString)
        
        hi_there = Tk.Message(self.frame)
        hi_there["text"] = "\nNow Viewing Deck!\n"
        hi_there.pack(side = "top")
        
        # question = Tk.Message(self.frame)
    #     question["text"] = "Question: " + questionString
    #     question.pack(side = "top")
        
        # text = Tk.Message(self.frame)
#         text["text"] = "\nAnswer:\n"
#         text.pack(side = "top")
        
        questionGUI = Tk.Message(self.frame)
        questionGUI["fg"] = 'black'
        questionGUI["text"] = questionString + "\n"
        questionGUI.pack(side = "top")
        
        answerGUI = Tk.Message(self.frame)
        answerGUI["fg"] = 'white'  
        answerGUI["text"] = answerString + "\n"
        answerGUI.pack(side = "top")
        
        
        
        # answer = Tk.Button(self.frame, text="Show Answer", command=self.openFrame(answerGUI))
#         answer.pack(side = "top")


        answer = Tk.Button(self.frame, text="Flip")
        answer["command"] = lambda: self.openFrame(answerGUI, questionGUI)
        answer.pack(side = "top")

        # if answer:
#             self.openFrame(answerGUI)
        
        previousCard = Tk.Button(self.frame, text="Previous Card")
        previousCard.pack(side = "left")
        
        nextCard = Tk.Button(self.frame, text="Next Card")
        nextCard.pack(side = "right")
        
        quit = Tk.Button(self.frame, text="Quit Program", command=self.root.destroy)
        quit.pack(side = "bottom")
        
        menu = Tk.Button(self.frame, text="Back to Menu")
        menu.pack(side = "bottom")
        
        #answer.pack()
        #answerGUI.pack()
        #previousCard.pack()
        #nextCard.pack()
        #menu.pack()
        #quit.pack()
        #hi_there.pack()
 
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
    
    def openFrame(self, answerGUI, questionGUI):
        # self.hide()
#         otherFrame = Tk.Toplevel()
#         otherFrame.geometry("500x500")
#         otherFrame.title("Answer")
        
        if answerGUI["fg"] == 'white':
            answerGUI["fg"] = 'black'
        elif answerGUI["fg"] == 'black':
            answerGUI["fg"] = 'white'
            
        if questionGUI["fg"] == 'black':
            questionGUI["fg"] = 'white'
        elif questionGUI["fg"] == 'white':
            questionGUI["fg"] = 'black'
        
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
        
    def nextCards(self):
        nextCard.pack()
        
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
