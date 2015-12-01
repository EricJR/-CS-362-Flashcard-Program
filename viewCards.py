#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

######################################################
I will work on implementing the view card sometime later this week if I get the chance. 
Here is my P.CODE, feel free to give me any comments/advice/feedback. 

PSUEDO CODE:
implement showCard as a bool
obtain list of questions
obtain list of answers

bool showCard = false

if showcard == false:
          hide answer
elif showcard == true:
          show answer 

click button showCard = true

if click button nextCard
       increment array
       showCard == false
       
       
if click button previousCard
       decrement array
       showCard == false
       
       
if click button quitProgram
      exit program
#########################################################




Notes: 
1 card = 










# #-----------------
import os
import sys
import os.path  #Used to read / write files
import re       #Used for regular expressions (Predefined flashcards)
                #Used for GUI  //https://www.youtube.com/watch?v=uh6AdDX7K7U
                #Library to download: http://www.tcl.tk/software/tcltk/download.html
import tkinter as tk
#import tkinter
#from tkinter import *
#
# #-----------------


import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk


class MultiColumnListbox(object):
    """use a ttk.TreeView as a multicolumn ListBox"""

    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        s = """
        Now Viewing 'FlashCard[0]' Contents\t\t\t
        """
        msg = ttk.Label(wraplength="4i", justify="left", anchor="n",
            padding=(10, 2, 10, 6), text=s)
        msg.pack(fill='x')
        container = ttk.Frame()
        container.pack(fill='both', expand=True)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=card_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in card_header:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))

        for item in card_list:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(card_header[ix],width=None)<col_w:
                    self.tree.column(card_header[ix], width=col_w)

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
        int(not descending)))

# the test data ...

card_header = ['Question', 'Answer']

#We need to ignore the first element because it is the title
card_list = [
('Question 1[1]', 'Answer 1[2]') ,
('Question 2[3]', 'Answer 2[4]') ,
('Question 3[5]', 'Answer 3[6]')
]


if __name__ == '__main__':
    root = tk.Tk()
    root.title("View FlashCards")
    root.geometry("1000x600")
    listbox = MultiColumnListbox()
    root.mainloop()
