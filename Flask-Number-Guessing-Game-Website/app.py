from flask import Flask, jsonify, request, render_template
import numpy as np

app = Flask(__name__)

# 🎯 Generate a random number (1 to 100 (Can change))
number = np.random.randint(1, 101)
guess = None

@app.route('/')
def home():
    # Renders the frontend HTML
    return render_template('index.html')

# POST route: user submits a guess
@app.route('/api/guess', methods=["POST"])
def check_guess():
    global guess
    data = request.get_json()
    global number 
    # Validation checks
    if not data or "num" not in data:
        return jsonify({"error": "Missing number"}), 400

    try:
        guess = int(data["num"])
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

    print(f"number:{number}")# Compare guess with secret number
    if guess < number:
        result = "Too Low!"
    elif guess > number:
        result = "Too High!"
    else:
        number = np.random.randint(1,101)
        result = "🎉 Correct! You guessed the number! (Enter new number to try again)"

     

    return jsonify({
        "your_guess": guess,
        "result": result
    }), 200

# Optional GET route (if you want to view the current guess result)
@app.route('/api/status', methods=["GET"])
def status():
    print("Hello world")
    if guess is None:
        return jsonify({"message": "No guess made yet."}), 200
    return jsonify({"last_guess": guess}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5001)
