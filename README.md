# GP's Blackjack Affair
Blackjack-like Game created with Python

To play: download repository as a zip file. Save to computer in the desired directory. Open terminal and change to the appropriate directory. Run the script by entering 'python3 Blackjack.py' (if Python version 3.0 or later)

## Overview

You are desperate to invest in a KPCB backed company, but you currently have $0. Take your
chances to win more $$ for a KPCB company's series B round funding. 

## How To Play

**Object of the Game**

Your goal is to beat the dealer by getting your hand count as close to 21 as possible without going over 21. 

**Card Value**

An Ace is worth 1 or 11 points.
A face card is worth 10 points.
Any other card is worth its numeric value.

**Setup**

Each player is dealt 2 cards to start. You can only see one of the cards in the dealer's hand. Choose to either "hit" to recieve another card or to "stick" to keep your current hand. Remember, the goal is to get as close to 21 without going over. When both the dealer and the player are content with their cards or if you bust, the round will end and $ will be rewarded or deducted accordingly. 

## Scoring
+$5 Mil -- Blackjack [Exactly 21]

+$1 Mil -- Win [Closer to 21 than Dealer]

-$3 Mil -- Bust [Over 21]

## Design
The game is structured into four classes, makes use of the random module, and draws inspo from open-source game code.

**Card Class**

The Card constructor defines suit and value attributes. When a card object is printed, it will print "*value* *suit*".

**Deck Class**

The deck constructor creates a list of (suit, value) pairs with length 52, representing the 52 cards in a standard deck. 
The shuffle method utilizes the shuffle function from the random module to change the order of the list.
The deal method pops the first card in cards off of the list.

**Hand Class**

The hand constructor defines an array of cards in the hand, a value of those cards, and flags if the hand is the dealer or not.
The class contains methods to add a card to a hand, calculate the value of a hand, return the value of a hand, and display a hand by printing the cards in the hand. If the dealer's hand is printed, the first card is hidden.

**Game Class**

A Game's attributes keep track of scoring and randomly selects from a list of KPCB portfolio companies.
The play method outputs the initial game setup with one instance of a deck object and two instances of the hand object. The program will continue to run the game until 'game_over' is set to true. If the player indicates they would like to play again, 'game_over' is set to false and the loop continues. Else, the winnings/losings of the player will be presented and the program will terminate.

## Other
- No bust for dealer
- The program determines whether an ace is scored as a 1 or 11
