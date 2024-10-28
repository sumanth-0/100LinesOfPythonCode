# app.py
from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_fortune(name):
    fortunes = [
        f"{name}, the future looks bright, but so does your ability to wear sunglasses.",
        f"Today is a good day for {name} to start that hobby you’ve been putting off since last year.",
        f"{name}, you will find peace and tranquility in the least expected places—like your couch.",
        f"Remember, {name}, even the best of plans can go awry—just like your last haircut.",
        f"{name}, your kindness will come back to you—probably in the form of pizza delivery.",
        f"Great fortune awaits you, {name}. But first, you must finish that snack.",
        f"Expect the unexpected today, {name}. Maybe a dance party in the middle of the street?",
        f"{name}, your wisdom is like a fine wine: it gets better with age—unless it’s from that questionable box.",
        f"Adventure is out there, {name}, and it might just involve a trip to the fridge.",
        f"{name}, remember: life is short. Smile while you still have teeth!"
    ]
    
    return random.choice(fortunes)

@app.route('/', methods=['GET', 'POST'])
def index():
    fortune = ""
    if request.method == 'POST':
        name = request.form['name']
        fortune = generate_fortune(name)
    return render_template('index.html', fortune=fortune)

if __name__ == '__main__':
    app.run(debug=True)
