class GradeTracker:
    def __init__(self):
        self.syllabus = {}  # {category: weight}
        self.grades = {}  # {category: [list of grades]}
        self.target_grade = 0

    def add_category(self, category, weight):
        current_total_weight = sum(self.syllabus.values())
        if current_total_weight + weight > 100:
            print(f"Error: Adding '{category}' with weight {weight}% would exceed the total of 100%.")
            raise ValueError("Total weight exceeds 100%")
        self.syllabus[category] = weight
        self.grades[category] = []

    def enter_grade(self, category, grade):
        if category in self.syllabus:
            self.grades[category].append(grade)
        else:
            print(f"Category '{category}' not found in syllabus.")

    def set_target_grade(self, target):
        self.target_grade = target

    def current_grade(self):
        total_weight = 0
        total_grade = 0
        for category, grades in self.grades.items():
            if grades:
                average = sum(grades) / len(grades)
                weight = self.syllabus[category]
                total_weight += weight
                total_grade += average * weight / 100
        return total_grade * 100 / total_weight if total_weight > 0 else 0

    def required_grades_all_categories(self):
        current_score = self.current_grade()
        
        if self.target_grade <= current_score:
            print("You have already met or exceeded the target grade.")
            return

        for category, weight in self.syllabus.items():
            grades_in_category = self.grades.get(category, [])
            current_category_average = sum(grades_in_category) / len(grades_in_category) if grades_in_category else 0

            # Calculate required grade in each category
            required_total_in_category = (self.target_grade - current_score * (100 - weight) / 100) * 100 / weight
            
            if required_total_in_category > 100:
                print(f"To achieve an overall target grade of {self.target_grade}%, you would need {required_total_in_category:.2f}% in '{category}', which may not be possible.")
            else:
                print(f"To achieve an overall target grade of {self.target_grade}%, you need {required_total_in_category:.2f}% in '{category}'.")

# Instantiate and use the GradeTracker as before
tracker = GradeTracker()

# Input syllabus categories and their weights
num_categories = int(input("Enter the number of grading categories: "))
for _ in range(num_categories):
    category = input("Enter category name (e.g., Homework, Midterm): ")
    weight = float(input(f"Enter the weight (in %) for {category}: "))
    tracker.add_category(category, weight)

# Input grades for each category
for category in tracker.syllabus:
    print(f"\nEntering grades for {category} (weight: {tracker.syllabus[category]}%)")
    while True:
        grade_input = input(f"Enter a grade for {category} (or type 'done' to finish): ")
        if grade_input.lower() == "done":
            break
        try:
            grade = float(grade_input)
            tracker.enter_grade(category, grade)
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")

# Set target grade
target = float(input("\nEnter your target overall grade (in %): "))
tracker.set_target_grade(target)

# Calculate required grades for all categories
print("\nCalculating required grades across all categories:")
tracker.required_grades_all_categories()
