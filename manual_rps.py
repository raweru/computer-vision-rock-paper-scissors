import random

def get_computer_choice():
    moves = ["rock", "paper", "scissors"]
    computer_move =  random.choice(moves)
    return computer_move

def get_user_choice():
    user_move = input("Please choose Rock, Paper or Scissors: ").lower()
    return user_move
