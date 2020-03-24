# a program to practice coding.
# a program to model a basic game of blackjack.
import random
import sys
# getting the name of the user
name = input("what is your name: ")

class Card():
    def __init__(self):
        # outlining the the deck
        self.heart_deck = []
        self.spade_deck = []
        self.club_deck = []
        self.diamond_deck = []
        self.full_deck = []

    def generate_deck(self):
        # a function to generate the deck
        for i in range(1,14):
            if i == 1:
                self.heart_deck.append(('Heart', 'Ace'))
                self.spade_deck.append(('Spade', 'Ace'))
                self.club_deck.append(('Club', 'Ace'))
                self.diamond_deck.append(('Diamond', 'Ace'))
            elif i == 11:
                self.heart_deck.append(('Heart', 'Jack'))
                self.spade_deck.append(('Spade', 'Jack'))
                self.club_deck.append(('Club', 'Jack'))
                self.diamond_deck.append(('Diamond', 'Jack'))
            elif i == 12:
                self.heart_deck.append(('Heart', 'Queen'))
                self.spade_deck.append(('Spade', 'Queen'))
                self.club_deck.append(('Club', 'Queen'))
                self.diamond_deck.append(('Diamond', 'Queen'))
            elif i == 13:
                self.heart_deck.append(('Heart', 'King'))
                self.spade_deck.append(('Spade', 'King'))
                self.club_deck.append(('Club', 'King'))
                self.diamond_deck.append(('Diamond', 'King'))
            else:
                self.heart_deck.append(('Heart', f'{i}'))
                self.spade_deck.append(('Spade', f'{i}'))
                self.club_deck.append(('Club', f'{i}'))
                self.diamond_deck.append(('Diamond', f'{i}'))

        self.full_deck = self.heart_deck + self.spade_deck + self.diamond_deck + self.club_deck

        return self.full_deck

    def shuffle_deck(self):
        # a function to shuffle the deck

        return random.shuffle(self.full_deck)


# game logic
class Game(Card):
    def __init__(self):
        super().__init__()
        self.round = 0
        self.player_card = []
        self.dealer_card = []
        self.generate_deck()
        self.shuffle_deck()
        self.player_num_wins = 0
        self.dealer_num_wins = 0



    def gen_player_dealer_hand(self):
        # a function to deal out the cards to the dealer and the player
        print('--------------------------------------')
        print('Starting the deal')
        for i in range(self.counter, self.big_counter):
            # player gets even cards in deck list
            if i % 2 == 0:
                self.player_card.append(self.full_deck[i])
                # dealer gets odd cards in deck list. doing this to model how cards are dealt in the game
            else:
                self.dealer_card.append(self.full_deck[i])

    def unpacking_player_hand(self):
        # a function that unpacks the tuples in the list of the player so the players score can be counted.
         # unpacking the tuples in the player list so we can use the values
        for suit, card in self.player_card:
            print(f'{name}, you have a {card} of {suit}s')
            if card in ( "Jack" , 'Queen' , 'King'):
                card = 10
                self.player_score += card
            elif card == 'Ace':
                # input validation for the ace card. Confirming weather the user wants the ace to be a 1 or 11.
                while True:
                    try:
                        card = int(input(f'{name}, you currently have a {card} do you want to count this as a one or eleven '
                                     f'enter 1 for one or 11 for eleven: '))
                    except ValueError:
                        print('Please enter a 1 or 11: ')

                    if card not in (1,11):
                        print('You need to enter 1 or 11: ')
                        continue
                    else:
                        self.player_score += card
                        break
            else:
                card = int(card)
                self.player_score += card

    def unpacking_dealer_hand(self):

        # unpacking the tuples in the dealer list so we can use the values
        for suit, card in self.dealer_card[:1]:
            # showing only the dealers first card
            print(f'The dealer has a {card} of {suit}s')

        for suit, card in self.dealer_card:
            # unpacking the dealers list so that the value of the dealers hand can be calculated
            if card in ("Jack", 'Queen', 'King'):
                card = 10
                self.dealer_score += card
            elif card == 'Ace':
                card = 11
                self.dealer_score += card
            else:
                card = int(card)
                self.dealer_score += card

    def asking_hit_stand(self):
        # a function to ask the user if they want to hit or stand
        while True:
            try:
                answer = str(input(f'{name}, Your current score is {self.player_score}. Do you want to hit or stand: '))
            except ValueError:
                print("Please enter a string. Enter hit or stand")
                continue
            if answer not in ('hit','stand','Hit','Stand'):
                print('Please enter hit or stand')
                continue
            else:
                if answer in ('hit','Hit'):
                    self.counter = self.big_counter
                    self.big_counter = self.big_counter+1
                    # unpacking the persons newly acquired card so its value can be added to the users hand.
                    card_value = self.full_deck[self.counter:self.big_counter]
                    for suit,card in card_value:
                        print(f'{name}, you drew a {card} of {suit}s')

                        if card in('Jack','Queen','King'):
                            card = 10
                            self.player_score += card
                        elif card == 'Ace':
                            while True:
                                try:
                                    card = int(input(f'{name}, you currently have a {card} do you want to count '
                                        f'this as a one or eleven enter 1 for one or 11 for eleven: '))
                                except ValueError:
                                    print('Please enter a 1 or 11: ')

                                if card not in (1, 11):
                                    print('You need to enter 1 or 11: ')
                                    continue
                                else:
                                    self.player_score += card
                                    break
                        else:
                            card = int(card)
                            self.player_score += card
                            print(f'{name}, Your new score is {self.player_score}')
                    break

                else:
                    print(f"Okay, Ben your current hand value is {self.player_score}")
                    break

    def checking_dealer_score(self):
        # a function to make sure the dealer keeps drawing cards until his hand value is 17
        while self.dealer_score<17:
            self.counter = self.big_counter
            self.big_counter+=1
            # unpacking the newly acquired card to add the card value to the dealers hand value.
            card_value = self.full_deck[self.counter:self.big_counter]
            for suit,card in card_value:
                print(f"The dealer just drew a {card} of {suit}s ")
                if card in ('Jack','Queen','King'):
                    card = 10
                    self.dealer_score += card
                    print(f'The dealer now has a score of {self.dealer_score}')
                elif card == 'Ace':
                    card = 11
                    self.dealer_score += card
                    print(f'The dealer now has a score of {self.dealer_score}')
                else:
                    card = int(card)
                    self.dealer_score += card
                    print(f'The dealer now has a score of {self.dealer_score}')
        print(f'The value of the dealer hand is {self.dealer_score}')

    def cleaning_player_and_dealer_hand(self,list):
        # a function to clean the dealer and player hand before they are dealt new cards.
        while list:
            list.pop(0)

    def check_winner(self):
        # a function to check the winner of the round
        if self.player_score > 21 and self.dealer_score>21:
            print('You both lost that round your scores were both over 21')

        elif self.player_score <= 21 and self.dealer_score > 21:
            print(f'Congrats {name} you have won this round with a score of {self.player_score}'
                  f' while the dealer had a score of {self.dealer_score}')
            self.player_num_wins += 1

        elif self.player_score > 21 and self.dealer_score <= 21:
            print(f'I am sorry the dealer won this round your score was {self.player_score} while the dealers was '
                  f'{self.dealer_score}.')
            self.dealer_num_wins += 1

        elif self.player_score <= 21 and self.dealer_score <= 21:
            if self.player_score> self.dealer_score:
                print(f'Congrats {name} you have won this round with a score of {self.player_score}'
                      f' while the dealer had a score of {self.dealer_score}')
                self.player_num_wins += 1

            elif self.player_score == self.dealer_score:
                print(f'{name} you and the dealer both had the same value of hands. The dealers hand was worth '
                      f'{self.dealer_score} while yours was worth {self.player_score} so this round ends in a draw')

            else:
                print(f'I am sorry the dealer won this round your score was {self.player_score} while the dealers was '
                      f'{self.dealer_score}.')
                self.dealer_num_wins += 1
        # setting the counters so they are 4 integers away from each other and so that they don't skip over any cards
        # setting the player and dealer score back to zero
        self.counter = self.big_counter
        self.big_counter = self.big_counter + 4
        self.player_score = 0
        self.dealer_score = 0

    def calculate_total_wins(self):
        # a function to calculate who had the most wins.
        if self.player_num_wins> self.dealer_num_wins:
            print(f'Congrats {name} you have won the most rounds with a total of {self.player_num_wins} wins to the '
                  f'dealers {self.dealer_num_wins} wins')
        elif self.player_num_wins == self.dealer_num_wins:
            print(f'{name} you and the dealer tied with both of you having {self.player_num_wins} wins')

        else:
            print(f'I am sorry {name} you have lost to the dealer. The dealer had a total of {self.dealer_num_wins} wins '
                  f'while you only had {self.player_num_wins} wins')

    def function_calls(self):
        # a function that calls all the main functions that are use so i can make 1 function call in the main logic.
        self.gen_player_dealer_hand()
        self.unpacking_dealer_hand()
        self.unpacking_player_hand()
        self.asking_hit_stand()
        self.checking_dealer_score()
        self.check_winner()
        self.cleaning_player_and_dealer_hand(self.player_card)
        self.cleaning_player_and_dealer_hand(self.dealer_card)


    def game_logic(self):
        # a function where the main logic of the program in compiled.
        self.player_score = 0
        self.dealer_score = 0
        self.counter = 0
        self.big_counter = 4
        while self.round  < 1:
            self.round = int(input("How many hands of BlackJack would you like to play. You must choose 1 or greater: "))

        while self.round > 0:
            # we need to deal the 2 cards to the dealer and the player
            # checking to see if we have enough cards to deal and the potential for the dealer and player to
            # draw more cards
            if len(self.full_deck)> self.big_counter:
                self.function_calls()



            else:
                # telling the user there are not enough cards left and that they can end the game or reshuffle.
                while True:
                    try:
                        answer = str(input('There are not enough cards in the deck to continue this round.'
                                           'do you want to reshuffle the deck and continue the game or end the game'
                                           'right now. Enter yes to keep playing or no to end the game.'))
                    except ValueError:
                        print('You have to enter yes or no')
                        continue

                    if answer not in ('yes','no','y','n'):
                        print('Enter yes to continue the game or no to stop it right now')

                    else:
                        if answer in ('yes','y'):
                            print(f'Okay {name} we are reshuffling the deck')
                            self.shuffle_deck()
                            self.game_logic()
                            self.counter = 0
                            self.big_counter = 4
                        else:
                            if self.player_num_wins>self.dealer_num_wins:
                                print(f'Okay {name}. You won the game. you beat the dealer with a total '
                                      f'of {self.player_num_wins} wins while the dealer only had'
                                      f' {self.dealer_num_wins}')
                                sys.exit(0)
                            elif self.dealer_num_wins> self.player_num_wins:
                                print(f'Okay {name}. we are sad to see you go. Come back and play again.'
                                      f'You lost the game to the dealer. The dealer had a total of '
                                      f'{self.dealer_num_wins} wins while you had {self.player_num_wins} wins')
                                sys.exit(0)
                            else:
                                print(f'Okay {name}. We are sad to see you go. Come back and play again.'
                                      f'You and the dealer tied the game with both having {self.player_num_wins}')
                                sys.exit(0)

            self.round -= 1
        self.calculate_total_wins()

if __name__ == "__main__":

    ben_game = Game()
    ben_game.game_logic()
