# Testing to make it work in Terminal.
# Next steps: After this works, we can work on using tkinter with it.

# It needs edit, delete, and a few other features still. Those shouldn't be very hard to implement. After that, we
# simply need to make these things work with Tkinter.

from file_reader import read_from_file, write_to_file

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
    def __init__(self, title, description):
        self._title = title
        self._description = description
        self._cards = []
        
    def get_title(self):
        return self._title
    
    def get_description(self):
        return self._description
        
    def get_cards(self):
        return self._cards
        
    def add_card(self, term, definition):
        new_card = Flashcard(term, definition)
        self._cards.append(new_card)

    def __str__(self):
        return ("%s" % (self._title))
        
class FlashcardController:
    def __init__(self):
        self._decks = []
        
    def get_decks(self):
        return self._decks
        
    def new_deck(self, deckTitle, deckDescription):
        
        newDeck = Deck(deckTitle, deckDescription)
        self._decks.append(newDeck)
    
    def add_cards_to_deck(self, title):
        test_decks = self._decks
        add_cards_choice = "Y"
        
        for deck in test_decks:
            if deck.get_title() == title:
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
            

def main():
    debug = True
    
    # Testing the file system
    read_from_file()
    
    # Currently debugging and auto-creating some decks
    if (debug):
        controller = FlashcardController()
        title = "Eric's Deck"
        deck = "This is the description of Eric's Deck."
        controller.new_deck(title,deck)
        controller.add_cards_to_deck(title)
        title = "Deck Dos"
        deck = "Description Deck Dos, dawg."
        controller.new_deck(title,deck)
        controller.add_cards_to_deck(title)
        print (controller)
    else:
        controller = FlashcardController()
        choice = input("Would you like to make a new Deck? (Y/N): ")
        while choice != "N":
            title = input("Enter deck name: ")
            deck = input("Enter deck description: ")
            controller.new_deck(title,deck)
            controller.add_cards_to_deck(title)
            choice = input("Would you like to make a new Deck? (Y/N): ")
    
        print (controller)
        
    write_to_file(controller)
        
        
if __name__ == "__main__":
    main()
