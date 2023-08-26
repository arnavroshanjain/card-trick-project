"""
This file contains all the functions needed to build and control the deck of
cards.

Do not change the function definitions, only the function bodies. You may add
additional functions if you wish.
"""

# enter any imports you feel are relevant here
import random
def build_deck() -> list[tuple]:
    """
    Create and return a list represene g the 52 cards of a deck.
    Each card in the list should be a tuple of form (suit, value).
    For example the Ace of Spades would be represented by tuple ("Spades, "A").
        deck[0] might contain ("Spades", "2") (i.e. the 2 of Spades)
        deck[1] might contain ("Diamonds","A") (i.e. the Ace of Diamonds)
        and so on.

    :return: deck, a list of card tuples
    :rtype: list
    """

    # enter your code here
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [] #creates an array for the deck

    for i in suits:
        for j in cards:
            deck.append((j, i))   #adds a tuple for each card in the format (cards, suits)
    print(deck)
    random.shuffle(deck) #to shuffle the cards in the deck
    return deck

#print(build_deck())

# add any additional functions you feel are appropriate.
