#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

# TODO: The selected deck is currently hard coded to the deck w/ name "Test Deck". We need to make
# a button for each deck and select the deck that the user clicks. Also, this needs to be put into a class
# and made to be modular.

import tkinter as tk  # gives tk namespace
from flashcard_classes import *


 
controller = FlashcardController()
file_sys = FileSystemStorage()

file_sys.read_from_file(controller)

def add_item():
    listbox1.insert(tk.END, enter1.get())
    
def add_item2():
    listbox2.insert(tk.END, enter1.get())
    
def delete_item():
    try:
        # get selected line index
        index = listbox1.curselection()[0]
        listbox1.delete(index)
        listbox2.delete(index)
        
    except IndexError:
        pass
 
def get_list(event):
    # get selected line index
    index = listbox1.curselection()[0]
    # get the line's text
    seltext = listbox1.get(index)
    # delete previous text in enter1
    enter1.delete(0, 50)
    # now display the selected text
    enter1.insert(0, seltext)
    
    
def get_list2(event):
    # get selected line index
    index = listbox2.curselection()[0]
    # get the line's text
    seltext = listbox2.get(index2)
    # delete previous text in enter1
    enter1.delete(0, 50)
    # now display the selected text
    enter1.insert(0, seltext)
    
def set_list(event):
    try:
        index = listbox1.curselection()[0]
        # delete old listbox line
        listbox1.delete(index)
    except IndexError:
        index = tk.END
    # insert edited item back into listbox1 at index
    listbox1.insert(index, enter1.get())
    
def set_list2(event):
    try:
        index = listbox2.curselection()[0]
        # delete old listbox line
        listbox2.delete(index)
    except IndexError:
        index = tk.END
    # insert edited item back into listbox1 at index
    listbox2.insert(index, enter1.get())
        
  
# def sort_list():
#     temp_list = list(listbox1.get(0, tk.END))
#     temp_list.sort(key=str.lower)
#     # delete contents of present listbox
#     listbox1.delete(0, tk.END)
#     # load listbox with sorted data
#     for item in temp_list:
#         listbox1.insert(tk.END, item)

def save_list():
    global controller
    global file_sys
    # get a list of listbox lines
    temp_list1 = list(listbox1.get(0, tk.END))
    temp_list2 = list(listbox2.get(0, tk.END))

    for deck in controller.get_decks():
        #TODO: needs to be updated to the name of the deck clicked on by the user, rather than this hard coded one
        if deck.get_name() == "Test Deck":
            deck.remove_all_cards()
            for card in deck.get_cards():
                print("\tTerm: ",card.get_term(),"\n\tDef: ",card.get_definition())

            for i in range(len(temp_list1)):
                deck.add_card(temp_list1[i], temp_list2[i])
            break

    file_sys.write_to_file(controller)

root = tk.Tk()
root.geometry("1000x1000")
root.title("Edit Cards")

#root.text("lol", row=0, column=0)



# create the listbox (note that size is in characters)
# listbox1 = tk.Listbox(root, width=120, height=30)
# listbox1.grid(row=0, column=0)

#lol = Label(root, text = "Question \t\t Answer")

listbox1 = tk.Listbox(root, width=60, height=30)
listbox1.grid(row=0, column=0)

listbox2 = tk.Listbox(root, width=60, height=30)
listbox2.grid(row=0, column=2)


# listbox1 = tk.Listbox(root, width=60, height=30)
# listbox1.grid(row=0, column=2)

# listbox2 = tk.Listbox(root, width=20, height=20)
# listbox2.grid(row=0, column=0)
 
# create a vertical scrollbar to the right of the listbox
yscroll = tk.Scrollbar(command=listbox1.yview, orient=tk.VERTICAL)
yscroll.grid(row=0, column=1, sticky=tk.N+tk.S)
listbox1.configure(yscrollcommand=yscroll.set)


yscroll = tk.Scrollbar(command=listbox2.yview, orient=tk.VERTICAL)
yscroll.grid(row=0, column=1, sticky=tk.N+tk.S)
listbox2.configure(yscrollcommand=yscroll.set)
 
# use entry widget to display/edit selection
enter1 = tk.Entry(root, width=50, bg='cyan')
enter1.insert(0, 'Click on an item in the listbox')
enter1.grid(row=2, column=0)

# pressing the return key will update edited line
enter1.bind('<Return>', set_list)

# or double click left mouse button to update line
enter1.bind('<Double-1>', set_list)

# button to sort listbox
# button1 = tk.Button(root, text='Sort the listbox    ', command=sort_list)
# button1.grid(row=3, column=0, sticky=tk.W)

# button to save the listbox's data lines to a file
button2 = tk.Button(root, text='Save lines to file', command=save_list)
button2.grid(row=4, column=0, sticky=tk.W)

# button to add a line to the listbox
button3 = tk.Button(root, text='Add entry text to listbox', command=add_item)
button3.grid(row=3, column=0, sticky=tk.E)

# button to delete a line from listbox
button4 = tk.Button(root, text='Delete selected line     ', command=delete_item)
button4.grid(row=4, column=0, sticky=tk.E)


# button to add a line to the listbox
button6 = tk.Button(root, text='Add entry text to listbox', command=add_item2)
button6.grid(row=3, column=2, sticky=tk.E)



# load the listboxs with data

for deck in controller.get_decks():
    if deck.get_name() == "Test Deck":
        for card in deck.get_cards():
            listbox1.insert(tk.END, card.get_term())
            listbox2.insert(tk.END, card.get_definition())

 
# left mouse click on a list item to display selection
listbox1.bind('<ButtonRelease-1>', get_list)

listbox2.bind('<ButtonRelease-1>', get_list)

root.mainloop()
 
