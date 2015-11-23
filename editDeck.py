#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
import tkinter as tk  # gives tk namespace

#Edit Deck 

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
    # get a list of listbox lines
    temp_list1 = list(listbox1.get(0, tk.END))
    temp_list2 = list(listbox2.get(0, tk.END))
    # add a trailing newline char to each line
    temp_list1 = [flash for flash in temp_list1]
    temp_list2 = [flash + '\n' for flash in temp_list2]
    final_list = []
    for i in range(len(temp_list1)):
        item_to_append = temp_list1[i]+ "~" + temp_list2[i]
        final_list.append(item_to_append)
    
    # give the file a different name
    fout = open("flashCards.txt", "w")
    fout.writelines(final_list)
    fout.close()

# read the data file into a list
fin = open("flashCards.txt", "r")
flash_list = fin.readlines()
fin.close()

# strip the trailing newline char
flash_list = [flash.rstrip() for flash in flash_list]
 
root = tk.Tk()
root.geometry("875x875")
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



# load the listbox with data
for item in flash_list:
    listbox1.insert(tk.END, item)
    
# load the listbox with data
for item in flash_list:
    listbox2.insert(tk.END, item)
 
# left mouse click on a list item to display selection
listbox1.bind('<ButtonRelease-1>', get_list)

listbox2.bind('<ButtonRelease-1>', get_list)

root.mainloop()
