from RPS_Template import prediction
import numpy as np
import random

def play():
    def get_computer_choice():
        moves = ["Rock", "Paper", "Scissors"]
        computer_choice =  random.choice(moves)
        print(computer_choice)
        return computer_choice

    def get_prediction():
        # Prediction/Classification
        
        # Open the file in read mode
        with open('file.txt', 'r') as f:
            # Read the lines of the file and strip the newline characters
            lines = [line.strip() for line in f.readlines()]
        # Create an empty dictionary to store the indices and labels 
        labels = {}
        # Loop through the lines and split them into key-value pairs
        for line in labels:
            idx, label = line.split()
            labels[int(idx)] = label
        
        #class_names = open("labels.txt", "r").readlines()
        index = np.argmax(prediction)
        class_name = (class_names[index][2:], end="")
        confidence_score = prediction[0][index]
        # Print prediction and confidence score
        #print("Class:", class_name[2:], end="")
        #print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
        print(class_name)
        return (class_name)

    def get_winner(a, b):
        print("." + a + "." + b + ".")
        if a == "Rock" and b == "Paper":
            print("You won!")
            return b
        elif a == "Rock" and b == "Scissors":
            print("You lost!")
            return a
        elif a == "Paper" and b == "Rock":
            print("You lost!")
            return a
        elif a == "Paper" and b == "Scissors":
            print("You won!")
            return a
        elif a == "Scissors" and b == "Rock":
            print("You won!")
            return a
        elif a == "Scissors" and b == "Paper":
            print("You lost!")
            return a
        else:
            print("It's a tie!")

    a = get_computer_choice()
    b = get_prediction()
    get_winner(a, b)

play()
