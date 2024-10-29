# Import libraries
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Load pre-trained mask detection model and face detector
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
mask_model = load_model("mask_detector_model.h5")

def detect_and_predict_mask(frame):
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))

    faces_list, preds = [], []

    for (x, y, w, h) in faces:
        face = frame[y:y + h, x:x + w]
        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        face = cv2.resize(face, (224, 224))
        face = img_to_array(face)
        face = preprocess_input(face)
        faces_list.append(face)

    if faces_list:
        faces_list = np.array(faces_list, dtype="float32")
        preds = mask_model.predict(faces_list)

    return faces, preds

# Initialize video stream
video_stream = cv2.VideoCapture(0)

while True:
    ret, frame = video_stream.read()
    if not ret:
        break

    faces, preds = detect_and_predict_mask(frame)

    for (box, pred) in zip(faces, preds):
        (x, y, w, h) = box
        (mask, withoutMask) = pred
        label = "Mask" if mask > withoutMask else "No Mask"
        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    cv2.imshow("Face Mask Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_stream.release()
cv2.destroyAllWindows()
