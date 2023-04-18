import random

def get_computer_choice():
    moves = ["rock", "paper", "scissors"]
    computer_choice =  random.choice(moves)
    return computer_choice

def get_user_choice():
    user_choice = input("Please choose Rock, Paper or Scissors: ").lower()
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == "rock" and user_choice == "paper":
        print("You won!")
    elif computer_choice == "rock" and user_choice == "scissors":
        print("You lost!")
    elif computer_choice == "paper" and user_choice == "rock":
        print("You lost!")
    elif computer_choice == "paper" and user_choice == "scissors":
        print("You won!")
    elif computer_choice == "scissors" and user_choice == "rock":
        print("You won!")
    elif computer_choice == "scissors" and user_choice == "paper":
        print("You lost!")
    else:
        print("It's a tie!")
