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

    def spawn(self):
        self.cars.append(Car(random.choice(COLORS)))

    def update(self):
        if len(self.cars) < 10:
            self.spawn()
        for car in self.cars:
            car.move(STARTING_MOVE_DISTANCE)

