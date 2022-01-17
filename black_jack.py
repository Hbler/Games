### Pierian Data Udemy Course - Milestone 2 Project ###

'''
Here are the requirements:

    You need to create a simple text-based BlackJack game
    The game needs to have one player versus an automated dealer.
    The player can stand or hit.
    The player must be able to pick their betting amount.
    You need to keep track of the player's total money.
    You need to alert the player of wins, losses, or busts, etc...

And most importantly:

    You must use OOP and classes in some portion of your game. You can not just use functions in your game. 
    Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!

“Original Solution”: (is a jupyter notebook)
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/08-Milestone%20Project%20-%202/03-Milestone%20Project%202%20-%20Complete%20Walkthrough%20Solution.ipynb
'''

### Steps
# Define card, deck, and player classes -ok
# Create auxiliary functions
#   Get player name and amount for funds -ok
#   Get player bet -ok
#   Check for and handle Ace value -ok
#   Table: show cards to player -ok
#   Empty hands -ok
# Game
#   Generate deck and shuffle it -ok
#   Setup player and "House" -ok
#   Input - Get amount to bet and check balance -ok
#   Deal cards -ok
#   Check for ace
#   Check for bust
#   Show cards, hide one of the houses cards -ok
#   Get player action -ok
#       get input if ace -ok
#   House acts -ok
#        handle ace -ok
#   Update table: All cards player, all cards House -ok
#   Compare values, declare winner -ok
#   Empty hands -ok
#   Check player funds and deck length -ok
#   Ask for next round or new game -ok

### Imports

import random

### Global Objects

SUITS = ('Hearts','Diamonds','Spades','Clubs')
RANKS = ('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
VALUES = {'Ace':'choose','Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10}
ABBREVIATIONS = {'Ace':'Ac','Two':'02','Three':'03','Four':'04','Five':'05','Six':'06','Seven':'07','Eight':'08','Nine':'09','Ten':'10','Jack':'Ja','Queen':'Qu','King':'Ki'}
GAME_ON = True
ROUNDS = 0

### Classes

class Card:
    ''' Creates a card instance with suit and rank '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[self.rank]
        self.abbr = ABBREVIATIONS[self.rank]

    def __str__(self):
        return f'| {self.abbr} of {self.suit[0:2]} |'

class Deck:
    ''' Creates a deck with 52 card instances based on suits and ranks, can shuffle it self, and deal a card '''

    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                new_card = Card(suit, rank)
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Player:
    ''' Creates a player instance with name, wallet and a hand that can get one or multiple cards or discard them '''

    def __init__(self, name, funds = 100):
        self.name = name
        self.funds = funds
        self.hand = []

    def hand_total(self, cards):
        ''' Returns the total value of the hand, used only after clearing Aces and the "buying cards" process '''

        total = 0

        for card in cards:
            total += card.value
        
        return total

    def get_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)

    def discard(self):
        return self.hand.pop(0)

    def bet(self, amount):
        if amount > self.funds:
            print ('\nInsufficient funds.')
            return 'Whoops'
        else:
            self.funds -= amount
        return amount

    def win(self, amount):
        self.funds += amount
        print(f'${amount} was added to {self.name} funds')

    def __str__(self):
        return f'{self.name} currently has ${self.funds} of funds.'

class House(Player):

    def handle_ace(self, cards):
        ''' Decides Ace value based on hand value '''

        value = 0

        for card in cards:
            if card.value != 'choose':
                value += card.value
            
        if value <= 10:
            return 11
        else:
            return 1

    def check_value(self, cards, value):
        ''' Checks the value of the A.I. hand and returns action'''

        total = 0
        
        for card in cards:
            if card.value != 'choose':
                total += card.value
            else:
                if value <= 10:
                    card.value = 11
                    total += card.value
                else:
                    card.value = 1
                    total += card.value

        if total > 21:
            print(f'\nBust! {self.name} hand sums up to {total}.')
            return 'B'
        elif total < 18:
            return 'H'
        else:
            return 'W'


### Functions

def player_info():
    ''' Gets and checks player inputs for a name and the amount of funds '''

    name = ''
    amount = 0
    valid = False

    while not valid:

        try:
            name += input('Please enter your name ')
            if name.isalpha():
                pass
            else:
                name = ''
                print('\nOnly letters please.')
                continue
   
            amount += int(input('How much will you add to your game funds? '))

        except:
            name = ''
            amount = 0
            print('\nSomething is not right. Try again!\nField one must be text, field two must be number')

        else:
            valid = True
            return name, amount
            break

def get_bet(player):
    ''' Gets player input and validates it '''

    player_bet = 0
    valid = False

    while not valid:

        try:
            player_bet += int(player.bet(int(input('\nEnter your bet for this round: '))))
        except:
            player_bet = 0
            print('\nSomething went wrong. Try again')

        else:
            valid = True
            return player_bet
            break

def check_value_player(value):
    ''' Cheks the value of the player cards, informs if player bust, and lost round;
        Gets input for Hit of Stand if lower than 21, and waits if equal to 21.
    '''

    if value > 21:
        print(f'\nBust! Your hand sums to {value}.')
        return 'B'
    elif value < 21:
        action = ''
        actions = ('H','S')

        while action not in actions:
            choice = input(f'\nYou have {value}, will you Hit or Stand? (H / S) ')
            action = choice.upper().replace(' ','')

            if action not in actions:
                print("\nSorry, that's not a valid option")
            elif action == 'S':
                print(f'\nYou have {value}! Wait to see who wins this round...')

        return action
    else:
        print(f'\nYou have {value}! Wait to see if there is a draw...')
        return 'W'

def handle_ace_player():

    print('You got an Ace!')
    ace_value = 'wrong'
    values = ['1','01','11']

    while ace_value not in values:
        ace_value = input('Which value do you want to use ( 1 or 11 ) ')

        if ace_value not in values:
            print("\nSorry that's not a valid option.")        
    return int(ace_value)

def first_table(house, player):
    ''' Displays the first cards drwan on the round '''

    print(f'House Cards: {house.hand[0]}    | ** of ** |\n')
    print(f'\n Your Cards: {player.hand[0]}    {player.hand[1]}')

def second_table(house, player):

    house_display = 'House Cards: '
    player_display = '\n Your Cards: '

    for card in house.hand:
        house_display += '    ' + str(card)

    for card in player.hand:
        player_display += '    ' + str(card)

    print(house_display)
    print(player_display)

def empty_hand(player,discarded_list):
    
    while len(player.hand) != 0:
        discarded_list.append(player.discard())

    return discarded_list


### Game

while GAME_ON:

    ### Setup
    if ROUNDS == 0:
        game_deck = Deck()
        game_deck.shuffle()

        discard_pile = []
        round_bet = 0

        house_ai = House('House', 0)
        player_name, player_funds = player_info()
        game_player = Player(player_name, player_funds)


    ROUNDS += 1
    
    # Get bet amount for the round
    player_bet = get_bet(game_player)
    round_bet += player_bet


    # Deal cards
    for x in range(2):
        house_ai.get_cards(game_deck.deal_card())
        game_player.get_cards(game_deck.deal_card())

    # Check for ace
    for card in game_player.hand:
        if card.value == 'choose':
            card.value = handle_ace_player()
    
    for card in house_ai.hand:
        if card.value == 'choose':
            card.value = house_ai.handle_ace(house_ai.hand)

    # Display table: 2 cards Player, 1 card House
    print('\n' * 50)
    first_table(house_ai, game_player)
    
    # Get player action
    player_chose = False

    while not player_chose:
        hand_sum = game_player.hand_total(game_player.hand)
        player_action = check_value_player(hand_sum)

        if player_action == 'B':
            player_chose = True
            break
        elif player_action == 'H':
            game_player.get_cards(game_deck.deal_card())
            continue
        elif player_action == 'S' or player_action == 'W':
            player_chose = True

    # House acts
    house_done = False

    while not house_done:
        try:
            house_action = house_ai.check_value(house_ai.hand, house_ai.hand_total(house_ai.hand))
        
        except:
            for card in house_ai.hand:
                if card.rank == 'Ace':
                    card.value = house_ai.handle_ace(house_ai.hand)

            house_action = house_ai.check_value(house_ai.hand, house_ai.hand_total(house_ai.hand))
        
        else:
            if house_action == 'B':
                house_done == True
                break
            elif house_action == 'H':
                house_ai.get_cards(game_deck.deal_card())
                continue
            elif house_action == 'W':
                house_done = True
            
    # Update table: All cards player, all cards House
    print('\n' * 2)
    second_table(house_ai, game_player)
    
    # Compare values, declare winner
    player_round_total = game_player.hand_total(game_player.hand)
    house_round_total = house_ai.hand_total(house_ai.hand)
    
    if house_round_total <= 21 and house_round_total == player_round_total:
        print("\nIt's a draw! You get your bet back!")
        game_player.win(round_bet)
        round_bet = 0
        pass
    elif house_round_total == 21 and (player_round_total > house_round_total or player_round_total < house_round_total):
        print("\nYou lost!")
        house_ai.win(round_bet)
        round_bet = 0
        pass
    elif house_round_total < 21 and (player_round_total < house_round_total or player_round_total > 21):
        print("\nYou lost!")
        house_ai.win(round_bet)
        round_bet = 0
        pass
    elif house_round_total > 21 and player_round_total > 21:
        print("\nBoth busted, bet carries to next round!")
        pass
    else:
        print("\nYou won!")
        game_player.win(round_bet * 2 )
        round_bet = 0
        pass

    # Empty hands
    discard_pile = empty_hand(game_player, discard_pile)
    discard_pile = empty_hand(house_ai, discard_pile)

    # Check player funds and deck length, ask for next round or new game
    if game_player.funds == 0 and round_bet == 0:
        new_game = ''
        new_game_options = ('Y','N')

        while new_game not in new_game_options:
            choice = input(f"\nYou don't have any more funds. \nStart a new game? (Y / N) ")
            new_game = choice.upper().replace(' ','')

            if new_game not in new_game_options:
                print("\nSorry, that's not a valid option")
        
        if new_game == 'Y':
            
            print(f'\nYou played for {ROUNDS} rounds')
            print(f'\n{len(discard_pile)} cards were used during the game')
            print(f'\nAnd lost a total of {house_ai.funds} to the House \n')

            ROUNDS = 0
            continue
        else:
            print(f'\nYou played for {ROUNDS} rounds')
            print(f'\n{len(discard_pile)} cards were used during the game')
            print(f'\nAnd lost a total of {house_ai.funds} to the House \nThanks for playing!')
            GAME_ON = False
            break
    else:
        print(game_player)
        next_round = ''
        next_round_options = ('Y','N')

        while next_round not in next_round_options:
            choice = input(f"\nReady for the next round?  (Y / N) ")
            next_round = choice.upper().replace(' ','')

            if next_round not in next_round_options:
                print("\nSorry, that's not a valid option")
        
        if next_round == 'Y':
            if len(game_deck.cards) <= 4:
                game_deck = Deck()
                game_deck.shuffle()
            continue
        else:
            print(f'\nYou played for {ROUNDS} rounds')
            print(f'\n{len(discard_pile)} cards were used during the game')
            print(f'\nAnd lost a total of {house_ai.funds} to the House \nThanks for playing!')
            GAME_ON = False
            break

### code by Hbler
