import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

class ImageClassifier:
    def __init__(self):
        # Load the MobileNet model
        self.model = tf.keras.applications.MobileNetV2(weights='imagenet')

    def preprocess_image(self, img_path):
        """Load and preprocess the image."""
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
        return img_array

    def classify_image(self, img_path):
        """Classify the image and return the top predictions."""
        processed_image = self.preprocess_image(img_path)
        predictions = self.model.predict(processed_image)
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]
        return decoded_predictions

def main():
    classifier = ImageClassifier()
    
    while True:
        img_path = input("Enter the path to the image you want to classify (or 'exit' to quit): ")
        if img_path.lower() == 'exit':
            print("Exiting the image classifier.")
            break
        if os.path.isfile(img_path):
            predictions = classifier.classify_image(img_path)
            print("Top Predictions:")
            for i, (imagenet_id, label, score) in enumerate(predictions):
                print(f"{i + 1}: {label} - {score:.2f}")
        else:
            print("Invalid file path. Please try again.")

if __name__ == "__main__":
    main()
