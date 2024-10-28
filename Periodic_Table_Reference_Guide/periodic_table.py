class Element:
    """Class to represent a chemical element."""
    def __init__(self, atomic_number, symbol, name, atomic_weight):
        self.atomic_number = atomic_number
        self.symbol = symbol
        self.name = name
        self.atomic_weight = atomic_weight

    def display_info(self):
        """Display the information about the element."""
        return (f"{self.atomic_number}: {self.symbol} ({self.name}) - "
                f"Atomic Weight: {self.atomic_weight}")


class PeriodicTable:
    """Class to represent the periodic table."""
    def __init__(self):
        self.elements = self.create_elements()

    def create_elements(self):
        """Create a dictionary of chemical elements."""
        return {
            1: Element(1, 'H', 'Hydrogen', 1.008),
            2: Element(2, 'He', 'Helium', 4.0026),
            3: Element(3, 'Li', 'Lithium', 6.94),
            4: Element(4, 'Be', 'Beryllium', 9.0122),
            5: Element(5, 'B', 'Boron', 10.81),
            6: Element(6, 'C', 'Carbon', 12.011),
            7: Element(7, 'N', 'Nitrogen', 14.007),
            8: Element(8, 'O', 'Oxygen', 15.999),
            9: Element(9, 'F', 'Fluorine', 18.998),
            10: Element(10, 'Ne', 'Neon', 20.180),
            # More elements can be added here...
        }

    def display_periodic_table(self):
        """Display the periodic table."""
        for atomic_number, element in self.elements.items():
            print(element.display_info())

    def get_element_info(self, atomic_number):
        """Get specific element information by atomic number."""
        if atomic_number in self.elements:
            print(self.elements[atomic_number].display_info())
        else:
            print("Element not found.")


def main():
    """Run the periodic table reference guide."""
    periodic_table = PeriodicTable()
    
    while True:
        print("\nPeriodic Table Reference Guide")
        periodic_table.display_periodic_table()
        
        try:
            atomic_number = int(input("Enter atomic number for details (0 to exit): "))
            if atomic_number == 0:
                break
            periodic_table.get_element_info(atomic_number)
        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()
