from RPS_Template import prediction
import numpy as np

def get_prediction():
    class_names = ["Rock", "Paper", "Scissors", "Nothing"]
    predicted_class = np.argmax(prediction[0])
    print("Predicted class: ", class_names[predicted_class])

get_prediction()
