# Author: Eric Roe
# Comments still need to be added, but here is a brief introduction.

# Description:
# This currently handles reading and writing to the text file. It doesn't have any checking to make sure the
# file successfully opens. Reading from a file with improper format (outlined below) will not break anything,
# but it will not split the content up correctly.

# Future additions:
# This program needs to take the contents (currently split into variables that are printed to the screen) and
# actually add them to the deck. It is an easy task.

# TEXT FILE FORMAT:
# The text file is set up with "@@@" before Deck Title and "~~" between:
#   1) Deck Title and Deck Description
#   2) Card Term and Card Definition
#ex:
"""
@@@DECK TITLE~~DECK DESCRIPTION
CARD TERM~~CARD DEFINITION
CARD TERM2~~CARD DEFINITION2
@@@DECK TITLE2~~DECK DESCRIPTION2
CARD T~~CARD D
CARD T2~~CARD D2
"""
# There are no problems if any of these things are left blank. The parser will still work and simply have a blank
# <insert term name here>.


import re
import sys

def read_from_file():

    infile = input("Enter the name of the file which we'll read from: ")
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
                print ("\nDeck name: {}\nDeck description: {}".format(deck_name, deck_desc))
            except:
                card_term = line[0]
                card_def = line[1].replace('\n','')
                print ("\tCard term: {}\n\tCard definition: {}".format(card_term, card_def))
        else:
            card_term = line[0]
            card_def = line[1].replace('\n','')
            print ("\tCard term: {}\n\tCard definition: {}".format(card_term, card_def))
            
            
            
def write_to_file(ctrler):
    outfile = input("Enter the name of the file which we'll write to: ")
  
    with open(outfile, "w") as f:
        for deck in ctrler.get_decks():
            deck_print = "@@@" + deck.get_title() + "~~" + deck.get_description() + "\n"
            f.write(deck_print)
            for card in deck.get_cards():
                card_print = card.get_term() + "~~" + card.get_definition() + "\n"
                f.write(card_print)



# Below is just test stuff. It is not needed, but will be saved until the end.

"""
delimiters = "@@@", "~~"
example = "What color is the sky?~~Blue"
regexPattern = '|'.join(map(re.escape, delimiters))
for i in re.split(regexPattern, example):
    print (i, " ")
"""
#lines.append(writelines(words[1].strip() + '\n' for words in line_words if len(words)>1))
