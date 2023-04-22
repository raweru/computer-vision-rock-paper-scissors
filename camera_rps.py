import numpy as np
import random
import cv2
from keras.models import load_model

def play():
    global computer_wins
    global user_wins
    computer_wins = 0
    user_wins = 0
    
    def get_computer_choice():
        moves = ["Rock", "Paper", "Scissors"]
        computer_choice =  random.choice(moves)
        print(f"Computer chose: {computer_choice}")
        return computer_choice

    def get_prediction():
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

        # Define countdown animation function
        def countdown_animation(frame, seconds_left):
            # Draw countdown text on the frame
            font = cv2.FONT_HERSHEY_TRIPLEX
            text = str(seconds_left)
            textsize = cv2.getTextSize(text, font, 4, 5)[0]
            text_x = int((frame.shape[1] - textsize[0]) / 2)
            text_y = int((frame.shape[0] + textsize[1]) / 2)
            cv2.putText(frame, text, (text_x, text_y), font, 4, (0, 0, 255), 5)

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
        return labels[index]

    def get_winner(comp, user):
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
        else:
            print("It's a tie!")

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

play()
