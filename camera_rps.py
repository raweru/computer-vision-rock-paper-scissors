import numpy as np
import random
import cv2
from keras.models import load_model

def get_computer_choice():
    
    '''The function randomly selects and returns a move (Rock, Paper, or Scissors) for the computer.
    
    Returns
    -------
        the computer's choice of either "Rock", "Paper", or "Scissors".
    
    '''
    
    moves = ["Rock", "Paper", "Scissors"]
    computer_choice =  random.choice(moves)
    print(f"Computer chose: {computer_choice}")
    return computer_choice


def countdown_animation(frame, seconds_left):
    
    '''This function draws a countdown text on webcam feed using OpenCV library in Python.
    
    Parameters
    ----------
    frame
        The current frame of the video or image on which the countdown animation will be drawn.
    seconds_left
        The number of seconds left in the countdown. This parameter is used to generate the text that will
    be displayed on the frame.
    
    '''
    
    # Draw countdown text on the frame
    font = cv2.FONT_HERSHEY_TRIPLEX
    text = str(seconds_left)
    textsize = cv2.getTextSize(text, font, 4, 5)[0]
    text_x = int((frame.shape[1] - textsize[0]) / 2)
    text_y = int((frame.shape[0] + textsize[1]) / 2)
    cv2.putText(frame, text, (text_x, text_y), font, 4, (0, 0, 255), 5)


def get_prediction():
    
    '''This function loads a pre-trained Keras model and uses it to predict the label of an image captured
    from a webcam after a countdown animation.
    
    Returns
    -------
        the label of the predicted object in the final frame captured by the camera.
    
    '''
    
    model = load_model('keras_model_mat_2_day_night.h5')
    with open('labels.txt', 'r') as f:
        # Read the lines of the file and strip the newline characters
        lines = [line.strip() for line in f.readlines()]

    # Create an empty dictionary to store the indices and labels 
    labels = {}
    
    # Loop through the lines and split them into key-value pairs
    for line in lines:
        idx, label = line.split()
        labels[int(idx)] = label
    
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Set countdown timer
    countdown_time = 5  # seconds
    start_time = cv2.getTickCount() / cv2.getTickFrequency()

    # Start countdown
    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()
        
        # Check if frame was successfully captured
        if not ret:
            print("Unable to capture frame")
            break

        # Calculate time elapsed
        time_elapsed = (cv2.getTickCount() / cv2.getTickFrequency()) - start_time
        # Check if countdown has finished

        if time_elapsed >= countdown_time:
            break

        # Display countdown animation
        countdown_animation(frame, countdown_time - int(time_elapsed))
        # Display the frame
        cv2.imshow("Countdown", frame)
        # Wait for a key press
        key = cv2.waitKey(1)

        if key == ord('q'):
            break

    # Capture final frame
    ret, frame = cap.read()
    
    # Check if frame was successfully captured
    if not ret:
        print("Unable to capture frame")

    # Resize and normalize image
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    # Predict on final frame
    prediction = model.predict(data)
    index = np.argmax(prediction)
    #confidence_score = prediction[0][index]
    print(f"You chose: {labels[index]}")
    cap.release()
    cv2.destroyAllWindows()
    
    if labels[index] in ["Rock", "Paper", "Scissors"]:
        return labels[index]
    
    #  In case it predicts "Nothing"
    else:
        print("Please choose Rock, Paper or Scissors!")
        get_prediction()


def get_winner(comp, user):
    
    '''This function determines the winner of a rock-paper-scissors game between the computer and the user
    and updates the global variables for the number of wins for each player.
    
    Parameters
    ----------
    comp
        represents the computer's choice of rock, paper, or scissors
    user
        represents the user's choice of rock, paper, or scissors in a game against the computer.
    
    '''
    
    global computer_wins
    global user_wins
    
    if comp == "Rock" and user == "Paper":
        print("You won!")
        user_wins += 1
        
    elif comp == "Rock" and user == "Scissors":
        print("You lost!")
        computer_wins += 1
        
    elif comp == "Paper" and user == "Rock":
        print("You lost!")
        computer_wins += 1
        
    elif comp == "Paper" and user == "Scissors":
        print("You won!")
        user_wins += 1
        
    elif comp == "Scissors" and user == "Rock":
        print("You won!")
        user_wins += 1
        
    elif comp == "Scissors" and user == "Paper":
        print("You lost!")
        computer_wins += 1
        
    elif comp == user:
        print("It's a tie!")


def play():
    
    '''The function "play" sets the initial scores to 0 and runs a loop until either the computer or user
    wins three times, calling other functions to get user input and computer choice, and determine the
    winner of each round.
    
    '''
    
    global computer_wins
    global user_wins
    computer_wins = 0
    user_wins = 0
    
    while True:
        
        if computer_wins == 3:
            print(f"Game over! Computer won {computer_wins}:{user_wins}.")
            break
        
        elif user_wins == 3:
            print(f"Game over! You won {user_wins}:{computer_wins}.")
            break
        
        else:
            user = get_prediction()
            comp = get_computer_choice()
            get_winner(comp, user)


if __name__ == "__main__":
    play()