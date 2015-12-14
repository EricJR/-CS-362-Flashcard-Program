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
#  Purpose: This module calls the program.
#  File name: main.py
#  Status: Complete.
#References and credits
#  Credits: The internet for its vast knowledge of the library tkinter.
#Permissions
#  The source code is free for use by members of the CS-362 class.  Credit this source if you borrow executable statements from this program.  The instructions 
#  are free to use, but create your own comments.  The comments are intellectual property.
#
#===== Begin code area ===================================================================================================================================================

from flashcard_gui import *

def main():
    create = switchWindow()
    create.mainloop()

if __name__ == "__main__":
    main()
