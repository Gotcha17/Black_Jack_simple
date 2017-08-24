from Tkinter import *
from math import ceil
from random import randint
from tkFont import BOLD
from tkFont import Font
from tkMessageBox import askokcancel
from tkMessageBox import showwarning
from tkSimpleDialog import askinteger


# Card deck
class Deck(object):
    """
    ATTRIBUTES:
        decks: Integer of how many decks a 52 cards should be used for the game
    """
    cards = {'Ah': 11, 'Kh': 10, 'Qh': 10, 'Jh': 10, '10h': 10, '9h': 9, '8h': 8, '7h': 7, '6h': 6, '5h': 5,
             '4h': 4, '3h': 3, '2h': 2, 'At': 11, 'Kt': 10, 'Qt': 10, 'Jt': 10, '10t': 10, '9t': 9, '8t': 8,
             '7t': 7, '6t': 6, '5t': 5, '4t': 4, '3t': 3, '2t': 2, 'Ac': 11, 'Kc': 10, 'Qc': 10, 'Jc': 10,
             '10c': 10, '9c': 9, '8c': 8, '7c': 7, '6c': 6, '5c': 5, '4c': 4, '3c': 3, '2c': 2, 'Ap': 11,
             'Kp': 10, 'Qp': 10, 'Jp': 10, '10p': 10, '9p': 9, '8p': 8, '7p': 7, '6p': 6, '5p': 5, '4p': 4,
             '3p': 3, '2p': 2}

    # Instantiate
    def __init__(self, decks):
        self.decks = decks
        self.deck_cards = Deck.cards.keys() * decks

    # Draw a random card
    def draw_card(self):
        """Draws a random card from all cards in the game
        :return: Str with card, Int with card value
        """

        rnd_card = randint(0, len(self.deck_cards) - 1)
        card = self.deck_cards[rnd_card]
        self.deck_cards.remove(card)
        return card, Deck.cards[card]

    def shuffle(self):
        self.__init__(self.decks)


# Dealer
class Dealer(object):
    """Dealer Object
    ATTRIBUTES:
        balance: Int of casinos profit
        card_stack: Stores cards that dealer has drawn as strings
        card_stack_value: Total value of dealer's drawn cards
        blank_card: Str of dealer's second drawn card
        blank_card_value: Int of dealer's second drawn card value
    """

    def __init__(self):
        self.balance = 0
        self.card_stack = []
        self.card_stack_value = 0
        self.blank_card = ''
        self.blank_card_value = 0

    def add_card(self, card, value):
        card = card[:-1]
        self.card_stack.append(card)
        self.card_stack_value += value

    def clear_cards(self):
        self.card_stack = []
        self.card_stack_value = 0

    def add_blank_card(self, card, value):
        self.blank_card = card
        self.blank_card_value += value

    def reveal_blank_card(self):
        # Add blank card to dealer's card stack
        self.add_card(self.blank_card, self.blank_card_value)
        # Clear blank card
        self.blank_card = ''
        self.blank_card_value = 0


# Player
class Player(object):
    """Player Object
    ATTRIBUTES:
        name: Str with player name
        balance: Int with starting funds
        card_stack: stores cards that player has drawn as strings
        card_stack_value: total value of player's drawn cards
        bet: amount of funds player has bet in current round
    """

    def __init__(self, name='Player', balance=100):
        self.name = name
        self.balance = balance
        self.card_stack = []
        self.card_stack_value = 0
        self.bet = ''

    def add_balance(self, amount):
        self.balance += amount
        return self.balance

    def subtract_balance(self, amount):
        self.balance -= amount
        return self.balance

    def add_card(self, card, value):
        card = card[:-1]
        self.card_stack.append(card)
        self.card_stack_value += value

    def place_bet(self, amount):
        self.bet = amount

    def clear_bet(self):
        self.bet = ''

    def clear_cards(self):
        self.card_stack = []
        self.card_stack_value = 0


# Main GameGUI
class GameGUI(object):
    def __init__(self, master):
        self.master = master

        # Define general layout
        self.dealer_frame = Frame(self.master, bg='SkyBlue1')
        self.dealer_frame.pack(side=TOP)

        self.table_frame = Frame(self.master, bg='SkyBlue1')
        self.table_frame.pack(side=TOP)

        self.player_frame = Frame(self.master, bg='SkyBlue1')
        self.player_frame.pack(side=TOP)

        # Table frame layout

        # Space label
        blank_space = ''
        self.table_space_lbl = Label(self.table_frame, text=blank_space, width=18, height=2, bg='SkyBlue1')
        self.table_space_lbl.grid(row=0, column=0)
        self.table_space_lbl = Label(self.table_frame, text=blank_space, width=18, height=2, bg='SkyBlue1')
        self.table_space_lbl.grid(row=0, column=1)
        self.table_space_lbl = Label(self.table_frame, text=blank_space, width=18, height=2, bg='SkyBlue1')
        self.table_space_lbl.grid(row=0, column=2)
        self.table_space_lbl = Label(self.table_frame, text=blank_space, width=18, height=2, bg='SkyBlue1')
        self.table_space_lbl.grid(row=1, column=0)
        self.table_space_lbl = Label(self.table_frame, text=blank_space, width=18, height=2, bg='SkyBlue1')
        self.table_space_lbl.grid(row=1, column=2)
        self.table_space_lbl = Label(self.table_frame, text=blank_space, width=18, height=2, bg='SkyBlue1')
        self.table_space_lbl.grid(row=2, column=0)
        self.table_space_lbl = Label(self.table_frame, text=blank_space, width=18, height=2, bg='SkyBlue1')
        self.table_space_lbl.grid(row=2, column=1)
        self.table_space_lbl = Label(self.table_frame, text=blank_space, width=18, height=2, bg='SkyBlue1')
        self.table_space_lbl.grid(row=2, column=2)
        self.next_btn = Button(self.table_frame, text='Proceed to the next round', command=lambda: logic.next_round())
        self.next_btn.grid(row=1, column=1)
        self.next_btn.grid_remove()
        # Dealer frame layout

        # Right dealer frame for buttons
        self.dealer_frame_right = Frame(self.dealer_frame, bg='SkyBlue1')
        self.dealer_frame_right.pack(side=RIGHT)
        # Center dealer frame for the cards
        self.dealer_frame_center = Frame(self.dealer_frame, bg='SkyBlue1')
        self.dealer_frame_center.pack(side=RIGHT)
        # Left dealer frame for info
        self.dealer_frame_left = Frame(self.dealer_frame, bg='SkyBlue1')
        self.dealer_frame_left.pack(side=RIGHT)

        # Layout for dealer's center frame

        # Dealer's center top frame
        self.dealer_center_top = Frame(self.dealer_frame_center, bg='SkyBlue1')
        self.dealer_center_top.pack(side=TOP)

        # Dealer space label
        self.dealer_space_lbl1 = Label(self.dealer_center_top, text='', width=16, height=1, bg='SkyBlue1')
        self.dealer_space_lbl1.grid(row=0, column=0)
        # Dealer name label
        self.dealer_name_lbl = Label(self.dealer_center_top, text='Dealer',
                                     font=helv16, width=16, height=1, bg='SkyBlue1')
        self.dealer_name_lbl.grid(row=0, column=1)
        # Dealer space label
        self.dealer_space_lbl2 = Label(self.dealer_center_top, text='', width=16, height=1, bg='SkyBlue1')
        self.dealer_space_lbl2.grid(row=0, column=2)
        # Dealer label
        self.dealer_value_lbl = Label(self.dealer_center_top, text='Cards value:  0', width=12, height=1, bg='SkyBlue1')
        self.dealer_value_lbl.grid(row=1, column=0)
        self.dealer_space_lbl3 = Label(self.dealer_center_top, text='', width=16, height=1, bg='SkyBlue1')
        self.dealer_space_lbl3.grid(row=1, column=1)

        # Dealer's center bottom frame
        self.dealer_center_bottom = Frame(self.dealer_frame_center, bg='SkyBlue1')
        self.dealer_center_bottom.pack(side=TOP)
        self.card_space_lbl1 = Label(self.dealer_center_bottom, text='', width=2, height=1, bg='SkyBlue1')
        self.card_space_lbl1.grid(row=0, column=0)
        self.card_space_lbl2 = Label(self.dealer_center_bottom, text='', width=2, height=1, bg='SkyBlue1')
        self.card_space_lbl2.grid(row=0, column=1)
        self.card_space_lbl3 = Label(self.dealer_center_bottom, text='', width=2, height=1, bg='SkyBlue1')
        self.card_space_lbl3.grid(row=0, column=2)
        self.card_space_lbl4 = Label(self.dealer_center_bottom, text='', width=2, height=1, bg='SkyBlue1')
        self.card_space_lbl4.grid(row=1, column=1)
        self.card_space_lbl5 = Label(self.dealer_center_bottom, text='', width=2, height=1, bg='SkyBlue1')
        self.card_space_lbl5.grid(row=1, column=2)
        self.card_frame = Frame(self.dealer_center_bottom, width=16, height=1, bg='SkyBlue1')
        self.card_frame.grid(row=1, column=1)

        # Layout for the dealer's right frame
        self.quit_btn = Button(self.dealer_frame_right, text='Quit game!', command=lambda: self.master.destroy())
        self.quit_btn.pack(side=RIGHT)

        # Layout for dealer's left frame

        # Restart game button
        retry_btn = Button(self.dealer_frame_left, text='New game', command=lambda: logic.next_round(new_game=True))
        retry_btn.pack(side=RIGHT)

        # Next round button

    def next_round_enable(self):
        self.next_btn.grid()

    def next_round_disable(self):
        self.next_btn.grid_remove()

    def add_card_dealer(self, card):
        card_lbl = Label(self.card_frame, text=card, width=2, height=1, borderwidth=1, relief=RIDGE)
        card_lbl.pack(side=LEFT)

    def update_dealer_value(self, value):
        self.dealer_value_lbl['text'] = 'Cards value:  ' + str(value)

    def clear_dealer_cards(self):
        for widget in self.card_frame.winfo_children():
            widget.destroy()

    def clear_players(self):
        for widget in self.player_frame.winfo_children():
            widget.destroy()

    # Dealer's label holder for blank card
    def add_card_dealer_blank(self):
        self.blank_card = Label(self.card_frame, text='', width=2, height=1, borderwidth=1, relief=RIDGE)
        self.blank_card.pack(side=LEFT)

    def reveal_blank_card(self, card):
        self.blank_card.config(text=card)


class PlayerFrame(object):
    def __init__(self, player, frame, balance):
        self.player = player
        self.balance = balance
        # Sub player frames
        self.frame = frame
        self.player_frame_sub = Frame(self.frame, borderwidth=1, relief=GROOVE)
        self.player_frame_sub.pack(side=RIGHT)

        # Dividing PlayerFrame into 3 frames

        # Top frame for cards
        self.top_frame = Frame(self.player_frame_sub, width=18, height=1)
        self.top_frame.pack()
        self.top_frame_space = Label(self.top_frame, text='', width=1, height=1, anchor=W)
        self.top_frame_space.pack(side=LEFT)
        # Center frame for buttons and entry
        self.center_frame = Frame(self.player_frame_sub, borderwidth=1, relief=GROOVE)
        self.center_frame.pack(side=TOP)
        # Bottom frame just for displaying players cards
        self.bottom_frame = Frame(self.player_frame_sub, borderwidth=1, relief=GROOVE)
        self.bottom_frame.pack(side=TOP)

        # Player's value of cards label
        self.player_value_lbl1 = Label(self.center_frame, text='Cards value: ', width=10, height=1, anchor=W)
        self.player_value_lbl1.grid(row=0, column=0)
        self.player_value_lbl2 = Label(self.center_frame, text='0', width=8, height=1, anchor=W)
        self.player_value_lbl2.grid(row=0, column=1)
        # Player's name label in the top row
        self.player_label = Label(self.center_frame, text='Player' + str(player), width=10, height=2, anchor=W)
        self.player_label.grid(row=1, column=0)
        # Player's info label in the top row
        self.player_info_lbl = Label(self.center_frame, text='Bet!', width=8, height=2, anchor=W)
        self.player_info_lbl.grid(row=1, column=1)

        # Entry field for amount of money that player wants to bet
        self.entry = Entry(self.center_frame, text='', width=5, justify=RIGHT)
        self.entry.grid(row=2, column=0)
        self.entry.delete(0, END)
        self.entry.insert(0, '0')
        # Bet button, after bet amount has been entered
        self.place_btn = Button(self.center_frame, text='Place', width=6, height=2,
                                command=lambda: self.read_entry())
        self.place_btn.grid(row=2, column=1)

        # Player's balance name label
        self.balance_lbl_stat = Label(self.center_frame, text='Balance:', width=10, height=1, anchor=W)
        self.balance_lbl_stat.grid(row=3, column=0)
        # Players balance label
        self.balance_lbl = Label(self.center_frame, text=str(self.balance), width=6, height=1, anchor=W)
        self.balance_lbl.grid(row=3, column=1)

        # Bottom row with 'Hit me!' and 'Pass' buttons
        self.hitme_btn = Button(self.center_frame, text='Hit me!', width=6, height=2,
                                command=lambda: logic.deal_player(self.player))
        self.hitme_btn.grid(row=4, column=0)
        self.pass_btn = Button(self.center_frame, text='Stand', width=6, height=2,
                               command=lambda: logic.pass_btn(self.player))
        self.pass_btn.grid(row=4, column=1)

    def update_balance(self, balance):
        self.balance_lbl['text'] = str(balance)

    def update_player_value(self, value):
        self.player_value_lbl2['text'] = str(value)

    def add_card(self, card):
        card_lbl = Label(self.top_frame, text=card, width=2, height=1, borderwidth=1, relief=RIDGE)
        card_lbl.pack(side=LEFT)

    def info_label(self, string):
        self.player_info_lbl['text'] = string

    # Read entered value in to the bet entry
    def read_entry(self):
        # Error handling for non int inputs
        try:
            entry = int(self.entry.get())
        except ValueError:
            showwarning('Warning', 'Please put in an integer')
        else:
            logic.place_bet(self.player, entry)

    # Activate entry and put in specified value
    def update_entry(self, amount=0):
        self.entry.config(state=NORMAL)
        self.entry.delete(0, END)
        self.entry.insert(0, str(amount))

    def clear_cards(self):
        for widget in self.top_frame.winfo_children():
            widget.destroy()

    def disable_player(self):
        for widget in self.center_frame.winfo_children():
            widget.config(state=DISABLED)

    def enable_player(self):
        for widget in self.center_frame.winfo_children():
            widget.config(state=ACTIVE)


# Logic, structure and calculations of the game
class GameLogic(object):
    def __init__(self, player_amount, balance=100):
        # Initializing game GUI
        self.gui = GameGUI(root)

        # Dialog about how many players are going to be playing
        self.player_amount_backup = player_amount
        self.player_amount = player_amount

        # Starting funds of all players
        self.balance = balance

        # Turn counter
        self.turn = 0  # At the start of the game it is always Player1's turn

        # Initializing dealer object
        self.dealer = Dealer()

        # Initializing player objects depending on amount of players and storing tuples of objects in a list
        self.players = []
        for i in range(self.player_amount):
            self.players.append((Player('Player' + str(i + 1), self.balance),
                                 PlayerFrame(i, self.gui.player_frame, self.balance)))

        # Initialize Deck, for each player in the game two decks of cards are initialized
        self.game_deck = Deck(self.player_amount * 2)

    # Draw new card
    def draw_card(self):
        return self.game_deck.draw_card()

    # Dealing cards to players
    def deal_player(self, player, exception=False):
        # Player can get a new card, if it is his turn and every player has placed a bet
        if (self.turn == player and self.bets_control()) or exception:
            new_card, new_card_value = self.draw_card()
            self.players[player][0].add_card(new_card, new_card_value)
            self.players[player][1].add_card(new_card)
            self.ace_value_exception(self.players[player][0])
            self.check_player_cards(player)
            self.players[player][1].update_player_value(self.players[player][0].card_stack_value)

            # Check card stack for black jack

    def black_jack(self, player=0, dealer=False):
        if dealer:
            item = self.dealer
        else:
            item = self.players[player][0]
        if item.card_stack_value == 21:
            if len(item.card_stack) == 2:
                return True

    # Checks player cards value for bust, black jack or 21
    def check_player_cards(self, player):
        # Check for Black or 21
        if self.players[player][0].card_stack_value == 21:
            if self.black_jack(player):
                self.players[player][1].info_label('Black Jack!')
            else:
                self.players[player][1].info_label('21!')
            if self.turn == player:
                self.next_turn(player)
        # Check for bust
        if self.players[player][0].card_stack_value > 21:
            self.players[player][1].info_label('Busted!')
            self.next_turn(player)

    # Whenever a player finishes his move
    def next_turn(self, player):
        self.turn += 1
        if self.turn == self.player_amount:
            self.deal_dealer()
        elif self.players[player + 1][0].card_stack_value == 21:
            self.turn += 1
            if self.turn == self.player_amount:
                self.deal_dealer()
        else:
            self.players[player + 1][1].info_label('Move!')

    # Dealing cards to dealer
    def deal_dealer(self):
        # After all players have made their moves, dealer draws cards until his value of cards is >=17
        if self.turn > self.player_amount - 1 and self.dealer.card_stack_value > 0:
            # Retrieve blank card and its value
            self.gui.reveal_blank_card(self.dealer.blank_card)
            self.dealer.reveal_blank_card()
            # Check for ace exception
            self.ace_value_exception(self.dealer)
            while self.dealer.card_stack_value < 17:
                new_card, new_card_value = self.draw_card()
                self.dealer.add_card(new_card, new_card_value)
                self.gui.add_card_dealer(new_card)
                self.ace_value_exception(self.dealer)
            else:
                self.end_round()
        if self.dealer.card_stack_value == 0 and self.bets_control():
            new_card, new_card_value = self.draw_card()
            self.dealer.add_card(new_card, new_card_value)
            self.gui.add_card_dealer(new_card)
            new_card, new_card_value = self.draw_card()
            self.dealer.add_blank_card(new_card, new_card_value)
            self.gui.add_card_dealer_blank()
        self.gui.update_dealer_value(self.dealer.card_stack_value)

    # Checks whether or not all players have placed their bets
    def bets_control(self):
        bets_control = []
        for i in range(self.player_amount):
            bets_control.append(self.players[i][0].bet != '')
        return all(bets_control)

    # If bust and ace in the stack then count ace as 1 and not 11
    def ace_value_exception(self, dealer_player):
        if dealer_player.card_stack_value > 21 and ('A' in dealer_player.card_stack):
            dealer_player.card_stack_value -= 10
            dealer_player.card_stack.remove('A')  # removes ace for future check
            dealer_player.card_stack.append('A_')  # adds ace_ so history of card stack is complete

    # Places bet for specified player with given amount
    def place_bet(self, player, amount):
        # Player can only place bet if he hasn't done so already
        if self.players[player][0].bet == '':
            if amount > self.players[player][0].balance:
                bet_all = askokcancel(title='Insufficient funds',
                                      message='You can only bet ' + str(self.players[player][0].balance) + '!')
                if bet_all:
                    amount = self.players[player][0].balance
                else:
                    return False
            if amount < 1:
                bet_zero = askokcancel(title='Invalid bet', message='You must bet at least 1!')
                if bet_zero:
                    amount = 1
                else:
                    return False
            self.players[player][0].place_bet(amount)
            self.players[player][0].subtract_balance(amount)
            self.players[player][1].update_entry(amount)
            self.players[player][1].update_balance(self.players[player][0].balance)
            self.players[player][1].entry.config(state=DISABLED)
            self.players[player][1].place_btn.config(state=DISABLED)
        self.players[player][1].info_label('Wait')
        if self.bets_control():
            self.first_deal()

    # Dealing cards to players and dealer in the first round
    def first_deal(self):
        for j in range(2):  # Each player must get 2 cards first
            for i in range(self.player_amount):
                self.deal_player(i, exception=True)
                if i == self.turn:
                    self.players[i][1].info_label('Move!')
        self.deal_dealer()

    # If player does not want any additional cards, his turn is over
    def pass_btn(self, player):
        if self.turn == player and self.bets_control():
            self.players[player][1].info_label('Wait')
            self.next_turn(player)

    # Calculations at the end of each round
    def end_round(self):
        for i in range(self.player_amount):
            player = self.players[i][0]
            # Player has BJ and dealer not
            if self.black_jack(player=i) and not self.black_jack(dealer=True):
                # Ceil function is applied to float to get integers only
                player.add_balance(int(ceil(player.bet * 2.5)))
                self.players[i][1].info_label('Won: ' + str(int(ceil(player.bet * 2.5))) + '!')
            # Player and dealer have BJ
            elif self.black_jack(player=i) and self.black_jack(dealer=True):
                player.add_balance(player.bet)
                self.players[i][1].info_label('Tie!')
            # Other comparisons of final card stack values between player and dealer
            elif player.card_stack_value <= 21:
                if self.dealer.card_stack_value <= 21:
                    if player.card_stack_value > self.dealer.card_stack_value:
                        player.add_balance(player.bet * 2)
                        self.players[i][1].info_label('Won: ' + str(player.bet * 2) + '!')
                    elif player.card_stack_value == self.dealer.card_stack_value and not self.black_jack(dealer=True):
                        player.add_balance(player.bet)
                        self.players[i][1].info_label('Tie!')
                    else:
                        self.players[i][1].info_label('Lose :(')
                if self.dealer.card_stack_value > 21:
                    player.add_balance(player.bet * 2)
                    self.players[i][1].info_label('Won: ' + str(player.bet * 2) + '!')
            else:
                self.players[i][1].info_label('Lose :(')
        # Show next round button
        self.gui.next_round_enable()

    # Next round of the game or restart game with same amount of players and initial funds
    def next_round(self, new_game=False):
        if new_game:
            # Clear all player frames
            self.gui.clear_players()
            # Reset player object list
            self.players = []
            # Reset amount of players
            self.player_amount = self.player_amount_backup
            # Reinitialize player objects
            for j in range(self.player_amount):
                self.players.append((Player('Player' + str(j + 1), self.balance),
                                     PlayerFrame(j, self.gui.player_frame, self.balance)))
        else:
            players_lost = []
            for i in range(self.player_amount):
                self.players[i][1].info_label('Bet!')
                self.players[i][1].place_btn.config(state=ACTIVE)
                player = self.players[i][0]
                player_gui = self.players[i][1]
                player_gui.update_entry(player.bet)
                player.clear_bet()
                player.clear_cards()
                player_gui.update_player_value(0)
                player_gui.update_balance(player.balance)
                player_gui.clear_cards()
                if player.balance == 0:
                    players_lost.append(i)
            self.player_lose(players_lost)
        # Hide next round button
        self.gui.next_round_disable()
        # Reinitialise dealer
        self.reset_dealer()
        # Reset player turn
        self.turn = 0
        # Shuffle all cards
        self.game_deck.shuffle()

    # Player without funds cant continue playing
    def player_lose(self, players_lost):
        for player in players_lost:
            self.players[player][1].info_label('Bankrupt!')
            self.players[player][1].disable_player()  # Player frame is greyed out
            self.players.pop(player)  # Player objects are removed from list
            self.player_amount -= 1  # Amount of players is reduced by one
        # Player GUI objects must be reassigned
        if not len(self.players) == 0:
            for player_obj in self.players:
                player_obj[1].player = self.players.index(player_obj)
        else:
            restart = askokcancel(title='Bankruptcy',
                                  message='All players are bankrupt! Do you want to restart the game?')
            if restart:
                self.next_round(new_game=True)

    def reset_dealer(self):
        self.dealer.__init__()
        self.gui.clear_dealer_cards()
        self.gui.update_dealer_value(0)


# Creates main window
root = Tk()

w = 600  # width for the Tk root
h = 400  # height for the Tk root

# Get screen width and height
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen

# Calculate x and y coordinates for the Tk root window
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.title('Black Jack')  # Sets title of the main window

# Set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.configure(background='SkyBlue1')

# Setting font
helv16 = Font(family='Helvetica', size=16, weight=BOLD)

# Makes dialogs appear in front of the main windows and afterwards main windows is up front
root.deiconify()
root.lift()
root.focus_force()

# Starting game
player_n = askinteger("Number of players", "Put in number of players!")
logic = GameLogic(player_n, 1000)
root.mainloop()
