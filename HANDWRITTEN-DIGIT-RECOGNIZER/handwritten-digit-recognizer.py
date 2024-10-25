import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

def load_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape((60000, 28, 28, 1)).astype('float32') / 255
    x_test = x_test.reshape((10000, 28, 28, 1)).astype('float32') / 255
    return (x_train, y_train), (x_test, y_test)

def create_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def train_and_evaluate_model(model, x_train, y_train, x_test, y_test):
    model.fit(x_train, y_train, epochs=5, batch_size=64)
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print(f'\nTest accuracy: {test_acc:.4f}')

def predict_digit(model, x_test):
    index = np.random.randint(0, x_test.shape[0])
    image = x_test[index].reshape(28, 28)
    plt.imshow(image, cmap='gray')
    plt.title(f'Predicted: {np.argmax(model.predict(x_test[index].reshape(1, 28, 28, 1)))}')
    plt.show()

def main():
    (x_train, y_train), (x_test, y_test) = load_data()
    model = create_model()
    train_and_evaluate_model(model, x_train, y_train, x_test, y_test)
    predict_digit(model, x_test)

if __name__ == "__main__":
    main()
