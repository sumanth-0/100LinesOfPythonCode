
# Import libraries
import cv2
import numpy as np

# Load pre-trained models for age and gender detection
age_net = cv2.dnn.readNetFromCaffe("deploy_age.prototxt", "age_net.caffemodel")
gender_net = cv2.dnn.readNetFromCaffe("deploy_gender.prototxt", "gender_net.caffemodel")

# Define age and gender labels
age_ranges = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genders = ['Male', 'Female']

# Define function to detect age and gender
def detect_age_gender(image_path):
    frame = cv2.imread(image_path)
    blob = cv2.dnn.blobFromImage(frame, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)

    # Predict gender
    gender_net.setInput(blob)
    gender_preds = gender_net.forward()
    gender = genders[gender_preds[0].argmax()]

    # Predict age
    age_net.setInput(blob)
    age_preds = age_net.forward()
    age = age_ranges[age_preds[0].argmax()]

    # Display results on image
    label = f"{gender}, {age}"
    cv2.putText(frame, label, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.imshow("Age and Gender Detection", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run the function with an image
detect_age_gender("sample_image.jpg")
