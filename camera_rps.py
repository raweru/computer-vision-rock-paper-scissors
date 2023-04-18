from RPS_Template import prediction
import numpy as np

def get_prediction():
    class_names = ["Rock", "Paper", "Scissors", "Nothing"]
    predicted_id = int(np.argmax(prediction, axis=-1))
    predicted_class = class_names[predicted_id]
    print(predicted_class)

get_prediction()
