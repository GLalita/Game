import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return " ".join((self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in [u'\u2660', u'\u2663', u'\u2665',
                      u'\u2666'] for v in ["A", "2", "3", "4", "5", "6", 
                      "7", "8", "9", "10", "J", "Q", "K"]]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self):
        if self.dealer:
            print( u'\u1AD8' + " (hidden)")
            print(self.cards[1])
            if len(self.cards) > 2:
                print(self.cards[2])
        else:
            for card in self.cards:
                print(card)
            # print("Value:", self.get_value()) Turn on for an assist to player
            print()

class Game:
    def __init__(self):
        self.wins = 0
        self.blackjacks = 0
        self.loss = 0
        self.busts = 0
        self.portfolio = ["Peloton", "Beyond Meat", "Genentech", "Slack", "Nest"]
        self.company = self.portfolio[random.randint(0,4)]
        
    def get_wins(self):
        return self.wins

    def get_losses(self):
        return self.loss

    def get_cash(self):
        return self.wins*1 + self.blackjacks*5 - self.busts*3

    def play(self):
        playing = True
        print()
        print()
        print()
        print()
        print("-----------------------------------------")
        print("             "+  u'\u00AB' + u'\u2022' + "BLACKJACK" + u'\u2022' + u'\u00BB')
        print("-----------------------------------------")
        print("Win with the hand of cards closest to 21")
        print("...but dont go over 21 or you're BUSTED!")
        print("-----------------------------------------")
        print("You are starting with $0, take your")
        print("chances to win more $$ for a KPCB company")
        print("-----------------------------------------")
        print("Here's the scoop:")
        print("+$5 Mil -- Blackjack [Exactly 21]")
        print("+$1 Mil -- Win [Closer to 21 than Dealer]")
        print("-$3 Mil -- Bust [Over 21]")
        print("_________________________________________")

        while playing:
            print()
            print("Game On!")
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            print()
            print("Your hand is:")
            self.player_hand.display()
            print()
            print("Dealer's hand is:")
            self.dealer_hand.display()
            print()

            game_over = False

            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(
                        player_has_blackjack, dealer_has_blackjack)
                    continue
                choice = input("Please choose [Hit / Stick] ").lower()
                while choice not in ["h", "s", "hit", "stick"]:
                    choice = input("Please enter 'hit' or 'stick' (or H/S) ").lower()
                print("-----------------------------------------")
                # print(self.dealer_hand.value) Used to debug
                if self.dealer_hand.value < 15:
                    self.dealer_hand.add_card(self.deck.deal())
                    print()
                    print("Dealer's NEW hand is:")
                    self.dealer_hand.display()
                if choice in ['hit', 'h']:
                    self.player_hand.add_card(self.deck.deal())
                    print()
                    print("Your NEW hand is:")
                    self.player_hand.display()
                    if self.player_is_over() and (self.dealer_hand.value > 21):
                        print("Both of you BUSTED")
                        game_over = True
                    elif self.player_is_over():
                        print("----------------------------------") 
                        print("BUST--sorry, you just lost $30,000!")
                        print("----------------------------------") 
                        game_over = True
                        self.loss += 1
                        self.busts +=1
                else:
                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()

                    print()
                    print(u'\u00AB' + u'\u00AB' + "THE RESULTS ARE IN" + u'\u00BB' + u'\u00BB')
                    print("Your hand:", player_hand_value)
                    print("Dealer's hand:", dealer_hand_value)
                    print()

                    if player_hand_value > dealer_hand_value:
                        print("-----------------") 
                        print("WAHOO, YOU WIN!")
                        print("-----------------") 
                        print()
                        self.wins += 1
                    elif player_hand_value == dealer_hand_value:
                        print("Tie!")
                    else:
                        print("Dealer Wins!")
                        self.loss += 1
                    game_over = True

            print("---------- Wins:", self.get_wins()," --- Losses:", self.get_losses(), "----------")

            again = input("Play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
            print("-----------------------------------------")
            if again.lower() == "n":
                print()
                print("Thanks for playing!")
                if self.get_cash() < 0:
                    print("You lost $", abs(self.get_cash()), "Mil")
                    print("Time to pay up! Looks like " + self.company + " lost their funding.")
                else:
                    print("---------------------------------------------------------")
                    print("You won $", self.get_cash(), "Mil")
                    print("---------------------------------------------------------")
                    print("Just in time for " + self.company + " Series B funding!")
                    print("---------------------------------------------------------")
                print()
                playing = False
            else:
                game_over = False

    def player_is_over(self):
        return self.player_hand.get_value() > 21

    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True

        return player, dealer

    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack! Draw!")

        elif player_has_blackjack:
            self.blackjacks += 1
            print("You have BLACKJACK! You win $$ 5 Mil $$")
            print()

        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")

if __name__ == "__main__":
    game = Game()
    game.play()