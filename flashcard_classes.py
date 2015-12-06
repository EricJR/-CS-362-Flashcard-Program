import re
import sys
import os

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
        
    def add_card(self, term, definition):
        new_card = Flashcard(term, definition)
        self._cards.append(new_card)

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
                
    def __str__(self):
        #to_print = ""
        #for deck in self._decks:
        #    to_print += str(deck) + ", "
         
        #return ("%s" % (to_print[:-2]))
        
        # Convert the Deck objects in the decks[] list to str, and modify the string
        # with a comma between each object for easier reading.
        return (", ".join(map(str, self._decks)))









class FileSystemStorage:
    def __init__(self):
        self.file_name = "flashcards_file.txt"

        #filepath = os.path.join("/library",self.file_name)

        #subdir = os.path.join("/library/" + self.file_name)

        #try:
        #    os.mkdir(subdir)
        #except:
        #    print("failed")

        # Try to open the file. If it does not exist (first user run), it will be created. Otherwise, it confirms success.
        with open(self.file_name,"w+") as f:
            pass


    def get_file_name(self):
        return self.file_name

    def read_from_file(self, ctrler):
        infile = self.file_name
        file_lines = []
        RE_lines = []
        
        with open(infile, "r") as ifh:
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
                    #print ("\tCard term: {}\n\tCard definition: {}".format(card_term, card_def))
            else:
                card_term = line[0]
                card_def = line[1].replace('\n','')
                ctrler.get_deck(deck_name).add_card(card_term, card_def)
                #print ("\tCard term: {}\n\tCard definition: {}".format(card_term, card_def))

        return ctrler

    def write_to_file(self, ctrler):
        outfile = self.file_name
        #outfile = os.path.abspath("library/" + self.file_name)
      
        with open(outfile, "w") as f:
            for deck in ctrler.get_decks():
                deck_print = "@@@" + deck.get_name() + "~~" + deck.get_description() + "\n"
                f.write(deck_print)
                for card in deck.get_cards():
                    card_print = card.get_term() + "~~" + card.get_definition() + "\n"
                    f.write(card_print)
