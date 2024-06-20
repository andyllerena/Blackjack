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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards():
  while len(user_hand) < 2:
    random_card = random.choice(cards)
    user_hand.append(random_card)

  while len(cpu_hand) < 1:
    random_card = random.choice(cards)
    cpu_hand.append(random_card)

def card_counter(hand):
  total = sum(hand)
  return total

def game_rules():
  clear()
  print(logo)
  deal_cards()
  user_total = card_counter(user_hand)
  comp_total = card_counter(cpu_hand)
  print(f"User hand: {user_hand}, Current score: {user_total}\nCpu Hand: {cpu_hand}, Current score: {comp_total} ")

  while user_total <= 21:
      choice = input("Do you want to hit or stand? Type 'h' or 's': ").lower()
      if choice == 'h':
        random_card = random.choice(cards)
        user_hand.append(random_card)
        user_total = card_counter(user_hand)
        print(f"Your hand: {user_hand}, Current score: {user_total}\nFinal Cpu Hand: {cpu_hand}, Final score: {comp_total} ")

        if user_total > 21:
          print("You lose!")
        
      elif choice == 's':
        break
      else:
       print("Please enter a valid input Type 'h' or 's' ")

  while comp_total < 17:
    random_card = random.choice(cards)
    cpu_hand.append(random_card)
    comp_total = card_counter(cpu_hand)

  print(f"Final User hand: {user_hand}, Final score: {user_total}\nCpu Hand: {cpu_hand}, Current score: {comp_total} ")

  if comp_total > 21 or user_total > comp_total:
    print("You win!")
  elif user_total < comp_total:
    print("You lose!")
  else:
    print("It's a draw!")
    
  
while True:
  choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
  if choice == 'y':
    user_hand = []
    cpu_hand = []
    game_rules()
  elif choice == 'n':
    print("Goodbye!")
    break
  else:
    print("Please enter a valid input Type 'y' or 'n' ")
    
  





    
    
  










  



