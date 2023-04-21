from RPS_Template import prediction
import numpy as np

def get_prediction():
    class_names = open("labels.txt", "r").readlines()
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

get_prediction()
