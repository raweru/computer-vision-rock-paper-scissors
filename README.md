# Computer Vision RPS

## Milestone 1: Set up the environment

First thing starting this project was to setup and clone the Github repo, which was an easy task, as we done the same already in the previous project "Hangman".

## Milestone 2: Create the computer vision system

Creating the computer vision system was a a breeze using [Teachable Machine](https://teachablemachine.withgoogle.com/), which provides a simple way to record your data and train a deep learning model. Using our webcam, we recorded around 500 photos for each class (Rock, Paper, Scissors, Nothing), that were used to train the computer vision model.

After training was finished, we downloaded the model as "keras_model.h5" and "labels.txt" into the local repository and commit and push the changes to Github.

## Milestone 3: Install the dependencies

Before running the program, we need to install the dependencies. We will set up a virtual environment and install opencv-python, tensorflow, and ipykernel using pip install.

## Milestone 4: Create a Rock-Paper-Scissors game

## Task 1: Store the user's and computer's choices

This code needs to randomly choose an option (rock, paper, or scissors) and then ask the user for an input.

Create another file called manual_rps.py that will be used to play the game without the camera.

You will need to use the random module to pick a random option between rock, paper, and scissors and the input function to get the user's choice.

Create two functions: get_computer_choice and get_user_choice.

The first function will randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice.

The second function will ask the user for an input and return it.

```python
import random

def get_computer_choice():
    moves = ["rock", "paper", "scissors"]
    computer_choice =  random.choice(moves)
    return computer_choice

def get_user_choice():
    user_choice = input("Please choose Rock, Paper or Scissors: ").lower()
    return user_choice
```

### Task 2: Figure out who won

Using if-elif-else statements, the script should now choose a winner based on the classic rules of Rock-Paper-Scissors.

For example, if the computer chooses rock and the user chooses scissors, the computer wins.

Wrap the code in a function called get_winner and return the winner.

This function takes two arguments: computer_choice and user_choice.

If the computer wins, the function should print "You lost", if the user wins, the function should print "You won!", and if it's a tie, the function should print "It is a tie!".

```python
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
```

