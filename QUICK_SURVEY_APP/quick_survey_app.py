class Survey:
    def __init__(self, questions):
        self.questions = questions
        self.responses = []

    def conduct_survey(self):
        print("Welcome to the Quick Survey App!")
        print("Please answer the following questions:\n")
        
        for question in self.questions:
            response = input(question + " ")
            self.responses.append(response)

    def summarize_results(self):
        print("\nSurvey Results:")
        for i, question in enumerate(self.questions):
            print(f"{question} -> {self.responses[i]}")

def main():
    # Define survey questions
    questions = [
        "How satisfied are you with our service? (1-5)",
        "Would you recommend us to a friend? (yes/no)",
        "What improvements would you like to see?",
    ]

    survey = Survey(questions)
    
    # Conduct the survey
    survey.conduct_survey()
    
    # Summarize and display the results
    survey.summarize_results()

# Run the survey app
if __name__ == "__main__":
    main()
