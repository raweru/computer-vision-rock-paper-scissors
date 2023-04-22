import cv2
from keras.models import load_model
import numpy as np

model = load_model('keras_model_mat_2_day_night.h5')
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
# Release the capture and destroy all windows
cv2.waitKey(500)
cap.release()
cv2.destroyAllWindows()
