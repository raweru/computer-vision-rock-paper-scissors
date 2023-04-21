from RPS_Template import prediction
import numpy as np
import random

def play():
    def get_computer_choice():
        moves = ["Rock", "Paper", "Scissors"]
        computer_choice =  random.choice(moves)
        print(f"Computer chose: {computer_choice}")
        return computer_choice

    def get_prediction():
        with open('labels.txt', 'r') as f:
            # Read the lines of the file and strip the newline characters
            lines = [line.strip() for line in f.readlines()]
        # Create an empty dictionary to store the indices and labels 
        labels = {}
        # Loop through the lines and split them into key-value pairs
        for line in lines:
            idx, label = line.split()
            labels[int(idx)] = label
        index = np.argmax(prediction)
        #confidence_score = prediction[0][index]
        print(f"You chose: {labels[index]}")
        return labels[index]

    def get_winner(a, b):
        if a == "Rock" and b == "Paper":
            print("You won!")
        elif a == "Rock" and b == "Scissors":
            print("You lost!")
        elif a == "Paper" and b == "Rock":
            print("You lost!")
        elif a == "Paper" and b == "Scissors":
            print("You won!")
        elif a == "Scissors" and b == "Rock":
            print("You won!")
        elif a == "Scissors" and b == "Paper":
            print("You lost!")
        else:
            print("It's a tie!")

    a = get_computer_choice()
    b = get_prediction()
    get_winner(a, b)

play()
