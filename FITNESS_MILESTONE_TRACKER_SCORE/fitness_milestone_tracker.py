
class FitnessMilestoneTracker:
    def __init__(self):
        self.milestones = []

    def add_milestone(self, milestone):
        self.milestones.append(milestone)
        print(f"Milestone added: {milestone}")

    def show_milestones(self):
        print("\nFitness Milestones:")
        for index, milestone in enumerate(self.milestones, start=1):
            print(f"{index}. {milestone}")

def main():
    tracker = FitnessMilestoneTracker()
    print("Welcome to the Fitness Milestone Tracker!")

    while True:
        action = input("\nEnter 'add' to add a milestone or 'show' to view milestones (or 'quit' to exit): ").strip().lower()
        if action == 'add':
            milestone = input("Enter your milestone: ")
            tracker.add_milestone(milestone)
        elif action == 'show':
            tracker.show_milestones()
        elif action == 'quit':
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
