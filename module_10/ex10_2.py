class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print("Current floor:", self.current)

    def floor_down(self):
            if self.current > self.bottom:
                self.current -= 1
                print("Current floor:", self.current)

    def go_to_floor(self, floor):
        while self.current < floor:
            self.floor_up()

        while self.current > floor:
            self.floor_down()

class Building:
    def __init__(self, bottom, top, quantity):
        self.bottom = bottom
        self.top = top
        self.quantity = []

        for i in range(quantity):
            elevator = Elevator(bottom, top)
            self.quantity.append(elevator)

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.quantity[elevator_number - 1]
        elevator.go_to_floor(destination_floor)

b = Building(1, 40, 6)

b.run_elevator(1, 8)
b.run_elevator(2, 15)
