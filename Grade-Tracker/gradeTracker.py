class GradeTracker:
    def __init__(self, target_grade=90):
        self.categories = {}
        self.target_grade = target_grade

    def add_category(self, name, weight, subcategories=None):
        # Add a new grade category with an optional list of subcategories.
        self.categories[name] = {"weight": weight, "grade": None}

    def add_grade(self, category_name, grade):
        # Add a grade to a specified category and subcategory.
        if category_name in self.categories:
            self.categories[category_name]["grade"] = grade
        else:
            print(f"Category '{category}' does not exist.")

    def current_grade(self):
        #Calculate the current total grade based on entered grades and weights.
        total_score = 0
        for category in self.categories.values():
            if category["grade"] is not None:
                total_score += category["grade"] * (category["weight"] / 100)
        return total_score

    def required_grades(self):
        #Calculate the grades needed in remaining categories to reach the target grade.
        current = self.current_grade()
        remaining_weight = sum(cat["weight"] for cat in self.categories.values() if cat["grade"] is None)
        if remaining_weight == 0:
            print("All categories have grades entered.")
            return None
        
        required = ((self.target_grade - current) * 100) / remaining_weight
        print(f"\nTo reach a target grade of {self.target_grade}%, you need an average of {required:.2f}% in remaining categories.")

    def display_progress(self):
        #Display current progress and required grades to reach the target grade.
        print("\nCurrent Grade Breakdown with Scores:")
        for name, category in self.categories.items():
            if category["grade"] is not None:
                score = category["grade"] * (category["weight"] / 100)
                print(f"{name} - {score:.2f}% of {category['weight']}% (Grade: {category['grade']}%)")
            else:
                print(f"{name} - No grade entered yet")
        
        print(f"\nTotal Grade: {self.current_grade():.2f}%")
        self.required_grades()

def main():
    # Set target grade
    target_grade = float(input("Enter your target grade (as a percentage, e.g., 85 for 85%): "))
    tracker = GradeTracker(target_grade)

    # Input categories until the weight is 100%
    total_weight = 0
    while total_weight < 100:
        print(f"\nRemaining weight to reach 100%: {100 - total_weight}%")
        category_name = input("Enter a category name (e.g., Assignment 1, Class Work, Midterm, Final,...): ")
        weight = float(input(f"Enter the weight for {category_name}: "))
        # Check for valid weight
        if weight <= 0 or total_weight + weight > 100:
            print(f"Invalid weight! Enter a positive value that doesn't exceed the remaining weight ({100 - total_weight}%).")
            continue

        # Add category to tracker
        tracker.add_category(category_name, weight)
        total_weight += weight

    print("\nCategories")
    while True:
        # Display category options for the user
        for i, (category_name, category) in enumerate(tracker.categories.items(), start=1):
            print(f"{i}. {category_name} (weight: {category['weight']}%)")

        selection = input("\nEnter the number of the category to add a grade, or type 'done' if finished: ").strip()
        if selection.lower() == 'done':
            break
        # Parse the selection and add grade
        try:
            category_index = int(selection) - 1
            category_name = list(tracker.categories.keys())[category_index]
            grade = float(input(f"Enter your grade for {category_name} (as percentage, e.g., 85): "))
            tracker.add_grade(category_name, grade)
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a valid category number.")

    tracker.display_progress() # Display progress and required grades

if __name__ == "__main__":
    main()