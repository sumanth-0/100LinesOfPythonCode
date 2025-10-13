"""Mini Handwriting Recognition
Load a pretrained MNIST model and predict handwritten digits from images.
Requires: tensorflow, numpy, pillow
"""

import numpy as np
from PIL import Image
import os

try:
    import tensorflow as tf
    from tensorflow import keras
except ImportError:
    print("Please install tensorflow: pip install tensorflow")
    exit(1)


class MiniHandwritingRecognizer:
    """Simple handwriting recognition using pretrained MNIST model."""
    
    def __init__(self):
        """Initialize and load pretrained MNIST model."""
        print("Loading MNIST model...")
        self.model = self._load_or_create_model()
        
    def _load_or_create_model(self):
        """Load pretrained MNIST model or create a simple one."""
        # Load MNIST dataset for training if model doesn't exist
        mnist = keras.datasets.mnist
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        
        # Normalize pixel values
        x_train, x_test = x_train / 255.0, x_test / 255.0
        
        # Create a simple neural network
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(10, activation='softmax')
        ])
        
        model.compile(optimizer='adam',
                     loss='sparse_categorical_crossentropy',
                     metrics=['accuracy'])
        
        # Train model briefly
        print("Training model...")
        model.fit(x_train, y_train, epochs=3, verbose=0)
        
        # Evaluate
        test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
        print(f"Test accuracy: {test_acc:.4f}")
        
        return model
    
    def preprocess_image(self, image_path):
        """Preprocess image to 28x28 grayscale format."""
        img = Image.open(image_path).convert('L')
        img = img.resize((28, 28))
        img_array = np.array(img)
        # Invert if needed (MNIST is white on black)
        if img_array.mean() > 127:
            img_array = 255 - img_array
        img_array = img_array / 255.0
        return img_array.reshape(1, 28, 28)
    
    def predict(self, image_path):
        """Predict digit from image."""
        img_array = self.preprocess_image(image_path)
        predictions = self.model.predict(img_array, verbose=0)
        predicted_digit = np.argmax(predictions[0])
        confidence = predictions[0][predicted_digit]
        return predicted_digit, confidence


if __name__ == "__main__":
    # Example usage
    recognizer = MiniHandwritingRecognizer()
    
    print("\nMini Handwriting Recognition Ready!")
    print("To use: recognizer.predict('path/to/digit_image.png')")
    print("\nTesting with MNIST sample...")
    
    # Create a sample test image from MNIST
    mnist = keras.datasets.mnist
    (_, _), (x_test, y_test) = mnist.load_data()
    sample_img = x_test[0]
    sample_label = y_test[0]
    
    # Save sample
    Image.fromarray(sample_img).save('test_digit.png')
    
    # Predict
    digit, conf = recognizer.predict('test_digit.png')
    print(f"Predicted: {digit}, Actual: {sample_label}, Confidence: {conf:.2%}")
