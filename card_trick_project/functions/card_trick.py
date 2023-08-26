"""
This file contains the functions that manipulate
the deck of cards to perform the trick.

Do not change the function definitions, only the function bodies. You may add
additional functions if you wish.

If you wish to use functions from another module in the functions folder,
you can use:
from . import <module_name>
and then:
<module_name>.<function_name>
"""

# enter any imports you feel are relevant he re
# from card_deck import build_deck

def fix_aces(deck: list) -> list[tuple]:
    """
    Puts the aces every 9 cards in the deck.
    :param deck: a list of card tuples
    :return: deck, a list of card tuples with aces strategically placed
    :rtype: list
    """
    # enter your code here
    aces = []  # creates deck to store aces
    j = 0  # intializes the j variable
    while j in range(len(deck)): #runs loop for through every card in the deck
    # for j in deck:  # using a for loop, caused the code to skip the next card after removing an ace.
                        # So when two aces apperard next to each other it skipped the second ace.
    # if j[0] == 'A':
        current_card = deck[j]
        if current_card[0] == 'A': #if any tuple in the deck has the Ace card, it enters the if statement
            aces.append(current_card)
            deck.remove(current_card)
            j -= 1
        j = j + 1
    #print(aces) # to test program, while I was building it

    ace_index = 0
    index = 8
    while len(aces) > 0: #enters loop when length of Array is greater than zero
        deck.insert(index, (aces[ace_index])) #inserts the ace card, at every 9th Position
        del aces[ace_index]
        index = index + 9

    return deck

# deck=fix_aces(build_deck())

def get_magic_card(deck: list, chosen_number) -> tuple[tuple, list]:
    """
    Given a number chosen by an audience member, this function will take the
    chosen number of cards from the deck and place in a 'new pile'.
    Then, the two digits from the audience's chosen number are added together
    (e.g. if chosen number is 13, then 1+3 == 4), and this number of cards are
    returned to the top of the deck.
    The next card in the new pile is the 'magic card'. The remaining cards in
    the new pile are returned to the bottom of the deck.
    This function returns both the 'magic card' and the adjusted deck.

    :param deck: a list of card tuples
    :param chosen_number: the number chosen by an audience member
    :return: a magic card tuple, and the deck list
    :rtype: tuple
    """
    new_pile = []
    print(f"I will now take {chosen_number} cards and place them in a new pile")
    for i in range(chosen_number):
        new_pile.append(deck.pop(0))  # removing card from deck and adding to new pile

    print("This is the New Pile:", new_pile)
    print("===========================================================================================================")
    #above line and other lines with "=" is to allow clarity when runnning program on command prompt
    print("This is the current deck:", deck)
    print("===========================================================================================================")

    sum_digits = 0
    for digit in str(chosen_number): #to get the sum digits, for eg: if users enters 12, sum will be 3
        sum_digits += int(digit)
    # print(sum_digits)

    print(f"To further randomise the selection, I will add the digits of your chosen numberv({chosen_number})together "
          f"and put that many cards from the new pile back in the deck (That is {sum_digits}cards)")
    print("===========================================================================================================")


    for i in range(sum_digits): #runs loop for
        deck.insert(0, new_pile.pop()) #if sum_digit is 3, it will add 3 cards from the new_pile back into deck)
    print("This is the current deck:", deck)
    print("===========================================================================================================")
    print("This is the new pile:", new_pile)


    magic_card = new_pile.pop() #takes the first card from the new pile and sets is aside
    print("I will now set aside the first card of the new pile. This is the magic card, we will save this for the end:", magic_card)
    deck = deck + new_pile

    print("Now onto the next part, pick the next number")
    return magic_card, deck


# add any additional functions you feel are appropriate.
