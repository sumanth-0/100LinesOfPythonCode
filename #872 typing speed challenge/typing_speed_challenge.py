import random
import time

# 1. List of sentences
sentences = [
    "Python is a versatile programming language.",
    "OpenAI develops advanced AI models.",
    "Typing speed tests help improve accuracy and speed.",
    "Consistency is key to learning programming."
]

# 2. Pick a random sentence
sentence = random.choice(sentences)
print("Type this sentence:")
print(sentence)

# 3. Start timer
start_time = time.time()
typed_text = input()
end_time = time.time()

# 4. Calculate WPM
words = len(typed_text.split())
time_taken = end_time - start_time
wpm = (words / time_taken) * 60
print(f"Your typing speed is {wpm:.2f} WPM")

# 5. Calculate accuracy
correct_words = sum(1 for a, b in zip(sentence.split(), typed_text.split()) if a == b)
accuracy = (correct_words / len(sentence.split())) * 100
print(f"Accuracy: {accuracy:.2f}%")
