import re
import sys
import os

"""
        decks = ctrler.get_decks()
        for deck in decks:
            cards = deck.get_cards()
            for card in cards:
                print("Card info: {}\n{}".format(card.get_term(), card.get_definition()))
                #for card in deck.get_cards():
                #    print("Added card:\n",card)
"""

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
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._cards = []
        
    def get_name(self):
        return self._name
    
    def get_description(self):
        return self._description
        
    def get_cards(self):
        return self._cards

    def set_name(self, name):
        self._name = name

    def set_description(self, description):
        self._description = description
        
    def add_card(self, term, definition):
        new_card = Flashcard(term, definition)
        self._cards.append(new_card)

    def remove_card(self, term):
        for card in self._cards:
            if card.get_term() == term:
                self._cards.remove(card)

    def remove_all_cards(self):
        del self._cards[:]

    def __str__(self):
        return ("%s" % (self._name))
        
class FlashcardController:
    def __init__(self):
        self._decks = []
        
    def get_decks(self):
        return self._decks

    def get_deck(self, name):
        for deck in self._decks:
            if deck.get_name() == name:
                return deck
        return

    def new_deck(self, deckname, deckDescription):
        newDeck = Deck(deckname, deckDescription)
        self._decks.append(newDeck)
    
    def add_cards_to_deck(self, name):
        test_decks = self._decks
        add_cards_choice = "Y"
        
        for deck in test_decks:
            if deck.get_name() == name:
                while add_cards_choice != "N":
                    new_term = input("Enter card term: ")
                    new_definition = input("Enter card definition: ")
                    deck.add_card(new_term, new_definition)
                    add_cards_choice = input("Add more cards? (Y/N): ")
                #for card in deck.get_cards():
                #    print("Added card:\n",card)
    
    def delete_deck(self, deck_name_to_delete):
        for deck in self._decks:
            if deck.get_name() == deck_name_to_delete:
                self._decks.remove(deck)
                break

    def print_all_content(self):
        for deck in self._decks:
            print("Deck Name: ",deck.get_name(), "\nDeck Description: ", deck.get_description())
            for card in deck.get_cards():
                print("\tTerm:",card.get_term(), "\n\tDef:", card.get_definition())
                
    def __str__(self):
        return (", ".join(map(str, self._decks)))

class FileSystemStorage:
    def __init__(self):
        self.file_name = "flashcards_file.txt"

        # Try to open the file. If it does not exist (first user run), it will be created. Otherwise, it confirms success.
        with open(self.file_name,"a+") as f:
            pass

    def get_file_name(self):
        return self.file_name

    def read_from_file(self, ctrler):
        file_lines = []
        RE_lines = []
        
        if os.stat(self.file_name).st_size > 0: # file has content to read
            with open(self.file_name, "r") as ifh:
                for line in ifh:
                    file_lines.append(line)
                    
            pattern = re.compile(r"@@@|~~")
            
            for line in file_lines:
                RE_lines.append(pattern.split(line))
                
            for line in RE_lines:
                if line[0] == '':
                    try:
                        deck_name = line[1]
                        deck_desc = line[2].replace('\n','')
                        ctrler.new_deck(deck_name, deck_desc)
                    except:
                        card_term = line[0]
                        card_def = line[1].replace('\n','')
                        ctrler.get_deck(deck_name).add_card(card_term, card_def)
                else:
                    card_term = line[0]
                    card_def = line[1].replace('\n','')
                    ctrler.get_deck(deck_name).add_card(card_term, card_def)
        else: # file is empty, so we don't read from it
            pass

        return ctrler

    def write_to_file(self, ctrler):
        open(self.file_name,"w").close()
        with open(self.file_name, "w") as f:
            for deck in ctrler.get_decks():
                deck_print = "@@@" + deck.get_name() + "~~" + deck.get_description() + "\n"
                f.write(deck_print)
                for card in deck.get_cards():
                    card_print = card.get_term() + "~~" + card.get_definition() + "\n"
                    f.write(card_print)
