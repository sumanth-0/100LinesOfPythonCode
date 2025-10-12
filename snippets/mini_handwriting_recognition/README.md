# Mini Handwriting Recognition

A simple Python script that implements handwriting recognition using a pretrained MNIST model. The script can recognize handwritten digits (0-9) from images.

## Description

This snippet demonstrates how to:
- Load and train a simple neural network on the MNIST dataset
- Preprocess handwritten digit images for recognition
- Make predictions with confidence scores
- Test the model with sample images

## Requirements

```bash
pip install tensorflow numpy pillow
```

## Usage

### Basic Example

```python
from mini_handwriting_recognition import MiniHandwritingRecognizer

# Initialize the recognizer
recognizer = MiniHandwritingRecognizer()

# Predict a digit from an image
digit, confidence = recognizer.predict('path/to/digit_image.png')
print(f"Predicted digit: {digit} (Confidence: {confidence:.2%})")
```

### Running the Script

```bash
python mini_handwriting_recognition.py
```

The script will:
1. Load and train a simple MNIST model
2. Create a test image from the MNIST dataset
3. Predict the digit and display the result

## Features

- **Simple Neural Network**: Uses a basic feedforward neural network with dropout
- **Image Preprocessing**: Automatically resizes and normalizes input images to 28x28 grayscale
- **Confidence Scores**: Provides prediction confidence for each digit
- **Quick Training**: Trains on MNIST dataset in just 3 epochs

## How It Works

1. **Model Architecture**: 
   - Flatten layer (28x28 → 784)
   - Dense layer (128 neurons, ReLU activation)
   - Dropout layer (0.2)
   - Output layer (10 neurons, Softmax activation)

2. **Image Processing**:
   - Converts images to grayscale
   - Resizes to 28x28 pixels
   - Inverts colors if needed (MNIST expects white digits on black background)
   - Normalizes pixel values to [0, 1]

3. **Prediction**:
   - Processes the image through the neural network
   - Returns the predicted digit and confidence score

## Example Output

```
Loading MNIST model...
Training model...
Test accuracy: 0.9765

Mini Handwriting Recognition Ready!
To use: recognizer.predict('path/to/digit_image.png')

Testing with MNIST sample...
Predicted: 7, Actual: 7, Confidence: 99.87%
```

## Limitations

- Only recognizes single digits (0-9)
- Works best with images similar to MNIST format (white digits on black background)
- Requires TensorFlow/Keras to be installed

## References

- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)
- [TensorFlow/Keras Documentation](https://www.tensorflow.org/api_docs/python/tf/keras)

## Author

Contributed to 100LinesOfPythonCode repository.

## Issue Reference

Fixes issue #757 - Mini Handwriting Recognition
