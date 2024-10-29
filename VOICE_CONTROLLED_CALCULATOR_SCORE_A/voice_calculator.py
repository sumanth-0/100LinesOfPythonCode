
# Import libraries
import speech_recognition as sr
import pyttsx3
import re
import operator

# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)

# Operations dictionary
operations = {
    "plus": operator.add,
    "minus": operator.sub,
    "times": operator.mul,
    "divided by": operator.truediv
}

# Function to evaluate spoken math expression
def evaluate_expression(expression):
    expression = expression.lower()
    for word, func in operations.items():
        if word in expression:
            numbers = re.findall(r'\d+', expression)
            if len(numbers) == 2:
                num1, num2 = map(int, numbers)
                result = func(num1, num2)
                return f"The result is {result}"
    return "I couldn't understand the expression."

# Function to process voice input
def voice_calculator():
    with sr.Microphone() as source:
        tts_engine.say("Please say a math operation.")
        tts_engine.runAndWait()
        audio = recognizer.listen(source)
    try:
        expression = recognizer.recognize_google(audio)
        result = evaluate_expression(expression)
        tts_engine.say(result)
        tts_engine.runAndWait()
    except sr.UnknownValueError:
        tts_engine.say("Sorry, I didn't understand that.")
        tts_engine.runAndWait()

# Run the calculator
voice_calculator()
