import random

def get_computer_choice():
    
    '''The function "get_computer_choice" returns a randomly chosen move from a list of "Rock",
    "Paper", and "Scissors".
    
    Returns
    -------
        a randomly chosen move from the list of "Rock", "Paper", and "Scissors".
    
    '''
    
    moves = ["Rock", "Paper", "Scissors"]
    computer_choice =  random.choice(moves)
    
    return computer_choice


def get_user_choice():
    
    '''This function prompts the user to choose between Rock, Paper, or Scissors and returns their
    choice.
    
    Returns
    -------
        the user's choice of either "Rock", "Paper", or "Scissors".
    
    '''
    while True:
        user_choice = input("Please choose Rock, Paper or Scissors: ").capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Please choose either Rock, Paper, or Scissors")


def get_winner(computer_choice, user_choice):
    
    '''The function takes in two choices (computer and user) and determines the winner based on the
    rules of rock-paper-scissors.
    
    Parameters
    ----------
    computer_choice
        The choice made by the computer in a game of rock-paper-scissors.
    user_choice
        The choice made by the user, which can be "Rock", "Paper", or "Scissors".
    
    '''
    
    if computer_choice == "Rock" and user_choice == "Paper":
        print("You won!")
        
    elif computer_choice == "Rock" and user_choice == "Scissors":
        print("You lost!")
        
    elif computer_choice == "Paper" and user_choice == "Rock":
        print("You lost!")
        
    elif computer_choice == "Paper" and user_choice == "Scissors":
        print("You won!")
        
    elif computer_choice == "Scissors" and user_choice == "Rock":
        print("You won!")
        
    elif computer_choice == "Scissors" and user_choice == "Paper":
        print("You lost!")
        
    elif computer_choice == user_choice:
        print("It's a tie!")


def play():
    
    '''Plays the game by running the above functions.'''
    
    get_winner(get_computer_choice(), get_user_choice())


if __name__ == "__main__":
    play()