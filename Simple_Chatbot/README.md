Simple Rule-Based Chatbot
This is a basic, command-line chatbot written in Python. It uses a predefined set of rules (using if/elif/else statements) to respond to user input.

Description
The program welcomes the user and then enters a continuous loop, waiting for the user to type a message. It analyzes the input for specific keywords and provides a corresponding response. If no keywords are matched, it gives a generic "I don't understand" reply.

Features
Interactive Chat: Runs in a loop to allow for a continuous conversation.

Keyword Matching: Uses the in keyword to find keywords, making it flexible (e.g., "hello" and "hello there" are both recognized).

Rule-Based: Responds to a hard-coded set of rules:

Greetings (hello, hi, hey)

Well-being (how are you)

Identity (what is your name, who are you)

Capabilities (what can you do, help)

Farewells (bye, goodbye)

Randomized Responses: Uses the random library to vary its answers for greetings and fallbacks, making it feel less robotic.

Clean Exit: The user can stop the bot at any time by typing exit, quit, or bye.

Requirements
Python 3

That's it! The script uses only built-in Python libraries (random), so no external packages need to be installed.

How to Run
Save the code as a Python file (e.g., chatbot.py).

Open your terminal or command prompt.

Navigate to the directory where you saved the file.

Run the script using Python:

Bash

python chatbot.py
Start chatting with the bot.