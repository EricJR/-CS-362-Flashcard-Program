# Testing to make it work in Terminal.
# Next steps: After this works, we can work on using tkinter with it.

class Flashcard:
    def __init__ (self):
        self._term = ""
        self._definition = ""
    
    def get_term(self):
        return self._term
        
    def get_definition(self):
        return self._definition
        
    def set_term(self, user_term):
        self._term = user_term
        
    def set_definition(self, user_definition):
        self._definition = user_definition
    
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
        
    def add_card(term, definition):
        new_card = Flashcard()
        self._cards.append(new_card)

    def stuff(self):
        pass
        
        
class FlashcardController:
    def __init__(self):
        self._decks = []
        
    def new_deck(self, deckTitle, deckDescription):
        
        newDeck = Deck(deckTitle, deckDescription)
        self._decks.append(newDeck)
        
    def delete_deck(self):
        




def main():

    controller = FlashcardController()
    choice = raw_input("Would you like to make a new Deck? (Y/N)")
    if choice == 'Y':
        t = raw_input("Enter deck name: ")
        d = raw_input("Enter deck description: ")
        controller.new_deck(t,d)
        
        
        
        
if __name__ == "__main__":
    main()
