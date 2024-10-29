
# Import necessary libraries
import datetime
from flask import Flask, render_template

app = Flask(__name__)

# Sample data for the timeline
events = [
    {"date": "1776-07-04", "event": "Declaration of Independence"},
    {"date": "1865-04-09", "event": "End of the Civil War"},
    {"date": "1969-07-20", "event": "First Moon Landing"},
    {"date": "1989-11-09", "event": "Fall of the Berlin Wall"},
]

# Convert string date to datetime object
for event in events:
    event["date"] = datetime.datetime.strptime(event["date"], "%Y-%m-%d")

@app.route('/')
def index():
    return render_template('timeline.html', events=events)

if __name__ == "__main__":
    app.run(debug=True)
