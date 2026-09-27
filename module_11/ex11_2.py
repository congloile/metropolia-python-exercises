class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

car1 = Car("ABC-123", 142)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

print("Current speed:", car1.current_speed)

car1.drive(1.5)

print("Travelled distance:", car1.travelled_distance)

car1.accelerate(-200)

print("Final speed:", car1.current_speed)

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super(). __init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume

electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(45)
gasoline_car.accelerate(65)

electric_car.drive(3)
gasoline_car.drive(3)

print("Travelled distance of electric car:", electric_car.travelled_distance)
print("Travelled distance of gasoline car:", gasoline_car.travelled_distance)
