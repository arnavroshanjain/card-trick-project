"""
This file contains the function calls to perform the card trick.
This should be the only place you have code outside of functions
and the code you do write should (mostly) just call other functions, or
handle input/output.

Note: to call functions from the scripts within functions, you need to
include the module name; e.g. card_deck.build_deck()
"""

# enter any imports you feel are relevant here

from functions import card_deck, card_trick

print("Welcome, I will be showing you a cool card trick!")
print("I have a deck of cards as you can see!")
print("") #to create an empty line, allowing clarity when viewing program on command prompt
deck=card_deck.build_deck()
print("============================================================================================================")
print("I will now shuffle them. 3.....2.....1..... and shuffle!")
print("The shuffled deck is below:")
card_trick.fix_aces(deck)
print(deck)
print("============================================================================================================")
print("")
print("Now let's begin!")

chosen_number=0
result=[]
for i in range(4):
    while True: #validation for the user input
        try:
            chosen_number = int(input("Please enter a number between 10 and 19"))
        except ValueError:
            print("Please enter a valid integer 1-10")
            continue
        if chosen_number > 10 and chosen_number < 19:
            print(f'You have entered: {chosen_number}')
            break
        else:
            print('Please enter a valid number between 10-19 (10 and 19, not included)')
    #chosen_number = int(input("Please enter a number between 10 and 19"))
    result.append(card_trick.get_magic_card(deck, chosen_number)[0])
print("The four magic cards are...",result)



