

from fpdf import FPDF

class GreetingCardCreator:
    def __init__(self):
        self.pdf = FPDF()

    def create_card(self, message, occasion):
        self.pdf.add_page()
        self.pdf.set_font("Arial", 'B', 24)
        self.pdf.cell(0, 10, f"Happy {occasion}!", 0, 1, 'C')
        self.pdf.set_font("Arial", '', 16)
        self.pdf.multi_cell(0, 10, message, 0, 'C')
        self.pdf.output(f"{occasion}_Greeting_Card.pdf")
        print(f"Greeting card created for {occasion}!")

def main():
    creator = GreetingCardCreator()
    occasion = input("Enter the occasion (e.g., Birthday, Holiday): ")
    message = input("Enter your personalized message: ")
    creator.create_card(message, occasion)

if __name__ == "__main__":
    main()
