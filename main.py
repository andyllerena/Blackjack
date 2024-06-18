############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
from replit import clear
import random 

choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

print(logo)

is_playing = True 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_hand = []
cpu_hand = []
user_total = 0
comp_total = 0

random_user_card = random.sample(cards,2)
random_cpu_card = random.sample(cards,1)
user_hand.extend(random_user_card)
cpu_hand.extend(random_cpu_card)

if choice == 'y':
  total = sum(user_hand)
  if total == 21:
    print ("You win :)")
  print(f"Your cards: {user_hand}, current score: {total}\nComputer's first card: {cpu_hand}")

while user_total <= 21 and choice != 'n':
  choice = input("Type 'y' to get another card, type 'n' to pass:")
  if choice == 'y':
      random_user_card = random.sample(cards,1)
      user_hand.extend(random_user_card)
      user_total = sum(user_hand)
      if user_total == 21:
        print ("You win :)")
        
      print(f"Your cards: {user_hand}, current score: {user_total}\nComputer's first card: {cpu_hand}")
      if user_total > 21:
        print ("You lose :(")

while comp_total <= 21:
  random_cpu_card = random.sample(cards,1)
  cpu_hand.extend(random_cpu_card)
  comp_total = sum(cpu_hand)
  if comp_total == 21 and comp_total>user_total:
    print ("You lose :)\n")

print(f"Your final: {user_hand}, current score: {user_total}\nComputer's final hand: {cpu_hand}, final score: {comp_total}")
print("You win :)")









  



