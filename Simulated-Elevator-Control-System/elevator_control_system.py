class Elevator:
    def __init__(self, total_floors):
        self.current_floor = 0
        self.total_floors = total_floors
        self.direction = None

    def move_elevator(self, target_floor):
        if target_floor < 0 or target_floor >= self.total_floors:
            print("Invalid floor! Please select a valid floor.")
            return

        print(f"Moving from floor {self.current_floor} to floor {target_floor}.")
        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.current_floor += 1
                self.direction = "up"
            else:
                self.current_floor -= 1
                self.direction = "down"
            print(f"Elevator is now at floor {self.current_floor} ({self.direction}).")
        
        print(f"Arrived at floor {self.current_floor}.")

    def start(self):
        while True:
            try:
                target_floor = int(input(f"Current floor: {self.current_floor}. Enter target floor (0-{self.total_floors-1}) or -1 to exit: "))
                if target_floor == -1:
                    print("Exiting the elevator system.")
                    break
                self.move_elevator(target_floor)
            except ValueError:
                print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    total_floors = 10  # Set the number of floors
    elevator = Elevator(total_floors)
    elevator.start()
