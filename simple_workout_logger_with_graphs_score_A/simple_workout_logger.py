import matplotlib.pyplot as plt

def log_workout(workouts):
    """Logs the workout details."""
    print("Workout Logged:")
    for workout in workouts:
        print(f"Exercise: {workout['exercise']}, Weight: {workout['weight']} kg, Reps: {workout['reps']}, Duration: {workout['duration']} mins")

def create_graph(workouts):
    """Creates a graph of weights lifted over time."""
    exercises = [workout['exercise'] for workout in workouts]
    weights = [workout['weight'] for workout in workouts]

    plt.figure(figsize=(10, 5))
    plt.bar(exercises, weights, color='skyblue')
    plt.xlabel('Exercises')
    plt.ylabel('Weight (kg)')
    plt.title('Workout Progress')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    workouts = []
    while True:
        exercise = input("Enter exercise name (or type 'exit' to stop): ")
        if exercise.lower() == 'exit':
            break
        weight = float(input("Enter weight lifted (in kg): "))
        reps = int(input("Enter number of reps: "))
        duration = float(input("Enter workout duration (in mins): "))
        
        workouts.append({'exercise': exercise, 'weight': weight, 'reps': reps, 'duration': duration})

    log_workout(workouts)
    create_graph(workouts)

if __name__ == "__main__":
    main()
