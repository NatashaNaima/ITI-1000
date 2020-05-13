# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck): #done
     """(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     """
     dealer = []
     other = []
     other.append(deck[50])
     for i in range(0,50,2):
         dealer.append(deck[i])
         other.append(deck[i+1])
     return (dealer, other)
     

def remove_pairs(l): #Done
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs = []
    pure_deck = []
    pure_deck_clean = []
    for i in l: # isolating card values from suits
        card_value = i[0]
        pure_deck.append(card_value)
    for char in pure_deck: # removing pairs
        occurence = 0
        if pure_deck_clean.count(char) == 0: # check val been evaluated yet
            occurence = pure_deck.count(char)
            if occurence%2 == 1: # if odd set, keeps one card
                pure_deck_clean.append(char)
    for char in pure_deck_clean: # find cards of value in hand and adding to new hand
        card = pure_deck.index(char)
        no_pairs.append(l[card])
    
    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    for i in range(len(deck)):
        print(deck[i],end =" ")
    print(" ")
              
    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    return
    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''
     inp = input("Enter an integer between 1 and " + str(n) + ": ")
     inputnum = 0
     
     valid = False
     while valid == False:
         if inp != "" and float(inp)%1 == 0:
             inputnum = int(inp)
         if 1<= inputnum <= n:
             valid = True
             return inputnum
         else:
            print("Invalid number.", end = " ")
            inp = input("Enter an integer between 1 and " + str(n) + ": ")
            valid = False

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     print("Your turn.")
     print("-------------")
     print("\n")
     print("Your current deck of cards is:")
     print_deck(human)
     print("\n")

     while len(human)>0 and len(dealer)>0: # until there is a winner
             #human turn
         print("I have", len(dealer), "cards. If 1 stands for my first cards and "
               + str(len(dealer)) + " for my last card, which of my cards would you like?")
         card_pos = get_valid_input(len(dealer))
         print('\n')
         print("You have asked my", card_pos, "th card.")
         card = dealer[card_pos-1]
         print("Here is is. It is", card)
         dealer.remove(card)
         human.append(card)
         print("\n")

         print("With", card, "added, your current deck of cards is:")
         print_deck(human)
         print("\n")
         dealer=remove_pairs(dealer)
         human=remove_pairs(human)
         print("After discarding the pairs and shuffling, your cards are:")
         print_deck(human)
         wait_for_player()

             #Dealer's turn
         print('my turn.')
         print("-----------")
         card_pos = random.randint(1,len(human))
         card = human[card_pos-1]
         print("I took your", card_pos, "th card.")
         human.remove(card)
         dealer.append(card)

         wait_for_player()

         print("Your turn.")
         print("------------")
         print("Your current deck of cards is:")
         print_deck(human)
         print("\n")


     print("Ups!", end = " ")
     if len(human) == 0:
         print("You do not have any more cards")
         print("Congratualations! You, Human, win.")
     else:
         print("I do not have any more cards.")
         print("You lost! I, Robot, win")
    
    
	 

# main
play_game()
