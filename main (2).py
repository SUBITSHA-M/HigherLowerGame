import random

from replit import clear

from art import logo, vs
from game_data import data


def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr},from {account_country}"
  
def check_answer(guess,a_follower,b_follower):
    if a_follower > b_follower:
      return guess == "a"
    else:
      return guess == "b"
      
def game():
       print(logo)
       score = 0
       game_should_continue = True
       account_a = get_random_account()
       account_b = get_random_account()
  
       while game_should_continue:
         account_a = account_b
         account_b = get_random_account()

         while account_a == account_b:
           account_b = get_random_account()
         print(f"Compare A: {format_data(account_a)}.")
         print(vs)
         print(f"Against B: {format_data(account_b)}.")
        
         guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
         a_follower_count = account_a["follower_count"]
         b_follower_count = account_b["follower_count"]
        
         is_correct = check_answer(guess,a_follower_count,b_follower_count)
         clear()
         print(logo)
         if is_correct:
          score+=1
          print(f"You're right! Current score: {score}.")
         else:
          game_should_continue = False
          print(f"Sorry, that's wrong. Final score: {score}.")
game()