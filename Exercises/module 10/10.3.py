class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Already at the top floor!")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Already at the bottom floor!")

    def go_to_floor(self, floor):
        if floor < self.bottom or floor > self.top:
            print("That floor does not exist in this building.")
            return

        print(f"Moving from floor {self.current_floor} to floor {floor}")

        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()

        print(f"Arrived at floor {self.current_floor}")

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]
        print(f"Building created with {num_elevators} elevators, floors {bottom} to {top}.")

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nRunning elevator #{elevator_number + 1}:")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number!")

    def fire_alarm(self):
        print("\n FIRE ALARM! All elevators returning to bottom floor! ")
        for i, elevator in enumerate(self.elevators):
            print(f"\nElevator #{i + 1} returning to bottom floor")
            elevator.go_to_floor(elevator.bottom)
        print("\nAll elevators are now at the bottom floor. Fire alarm protocol complete.")


if __name__ == "__main__":
    building = Building(1, 10, 3)
    building.run_elevator(0, 5)
    building.run_elevator(1, 8)
    building.run_elevator(2, 3)
    building.run_elevator(0, 1)
    building.fire_alarm()