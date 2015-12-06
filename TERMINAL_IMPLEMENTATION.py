# Testing to make it work in Terminal.
# Next steps: After this works, we can work on using tkinter with it.

from flashcard_classes import Flashcard, Deck, FlashcardController, FileSystemStorage

def main():
    controller = FlashcardController()
    file_sys = FileSystemStorage()
    debug = True
    
    # Testing the file system
    file_sys.read_from_file(controller)
    
    # Currently debugging and auto-creating some decks
    if (debug):
        title = "Eric's Deck"
        deck = "This is the description of Eric's Deck."
        controller.new_deck(title,deck)
        controller.add_cards_to_deck(title)
        title = "Deck Dos"
        desc = "Description Deck Dos, dawg."
        controller.new_deck(title, desc)
        controller.add_cards_to_deck(title)
        print (controller)
    else:
        choice = input("Would you like to make a new Deck? (Y/N): ")
        while choice != "N":
            title = input("Enter deck name: ")
            desc = input("Enter deck description: ")
            controller.new_deck(title, desc)
            controller.add_cards_to_deck(title)
            choice = input("Would you like to make a new Deck? (Y/N): ")
    
        print (controller)
        
    file_sys.write_to_file(controller)
        
        
if __name__ == "__main__":
    main()
