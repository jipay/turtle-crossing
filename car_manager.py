from car import Car
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.spawn()
        self.car_speed = STARTING_MOVE_DISTANCE

    def spawn(self):
        chance = random.randint(1, 6)
        if chance == 1:
            self.cars.append(Car(random.choice(COLORS)))

    def update(self):
        self.spawn()
        for car in self.cars:
            car.move(self.car_speed)

    def up_the_speed(self):
        self.car_speed += MOVE_INCREMENT