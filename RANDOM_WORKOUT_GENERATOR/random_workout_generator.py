import random

# Sample exercises for each muscle group
exercises = {
    'chest': ['Push-ups', 'Bench Press', 'Chest Fly'],
    'back': ['Pull-ups', 'Bent Over Rows', 'Deadlifts'],
    'legs': ['Squats', 'Leg Press', 'Lunges'],
    'arms': ['Bicep Curls', 'Tricep Dips', 'Hammer Curls'],
    'core': ['Planks', 'Sit-ups', 'Russian Twists']
}

def generate_workout(selected_muscle_groups, difficulty_level):
    workout = []
    for muscle in selected_muscle_groups:
        if muscle in exercises:
            num_sets = 3 if difficulty_level == 'easy' else 5
            selected_exercise = random.choice(exercises[muscle])
            workout.append(f"{selected_exercise}: {num_sets} sets")
    return workout

# User input
user_muscle_groups = ['chest', 'legs', 'arms']  # Example selection
difficulty = 'medium'  # Example difficulty level

# Generate workout
workout_plan = generate_workout(user_muscle_groups, difficulty)
for exercise in workout_plan:
    print(exercise)
