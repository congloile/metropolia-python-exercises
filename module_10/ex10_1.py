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

h = Elevator(1, 10)

h.go_to_floor(8)
h.go_to_floor(1)