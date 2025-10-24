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

        print(f"Moving from floor {self.current_floor} to floor {floor}...")

        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()

        print(f"Arrived at floor {self.current_floor}")


if __name__ == "__main__":
    h = Elevator(1, 10)
    h.go_to_floor(5)
    h.go_to_floor(1)