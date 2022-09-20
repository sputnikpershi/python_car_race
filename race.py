
"""
A static class to handle the events of a Car race
"""

# Local imports
from random import randint
from typing import List

import config
from car import Car


class CarRace:
    """Static class for the events of the car race"""

    cars: List[Car] = []
    number_of_cars: int = len(cars)
    is_race_active: bool = False
    number_of_seconds: int = 0

    @staticmethod
    def load_cars():
        """Load the Car objects, configure them and append them to the list"""

        # Create the "Consumer" (slow) cars
        for index in range(config.number_of_consumer_cars):
            consumer_car: Car = Car()
            decay_value: int = randint(config.speed_decay_range[0], config.speed_decay_range[1])
            speed: int = randint(config.speed_range_consumer_car[0], config.speed_range_consumer_car[0])
            consumer_car.speed = speed
            consumer_car.speed_factor = -decay_value
            consumer_car.name = f"consumer_car{index + 1}"
            CarRace.cars.append(consumer_car)

        # Create the "Sport" (fast) cars
        for index in range(config.number_of_sport_cars):
            sport_car: Car = Car()
            decay_value = randint(config.speed_increase_range[0], config.speed_increase_range[1])
            speed: int = randint(config.speed_range_sport_car[0], config.speed_range_sport_car[0])
            sport_car.speed = speed
            sport_car.speed_factor = decay_value
            sport_car.name = f"sport_car{index + 1}"
            CarRace.cars.append(sport_car)

        CarRace.is_race_active = True

    @staticmethod
    def start_race():

        while CarRace.is_race_active:
            CarRace.number_of_seconds += 1
            print(f"Car status: Time {CarRace.number_of_seconds} seconds")

            # Drive each, check if it has reached the goal
            for car in CarRace.cars:
                car.drive()
                print(f"- car: {car.name} has distance: {car.distance}")

                if car.distance >= config.max_distance:
                    print(f"- car: {car.name} has won the race!")
                    break

            CarRace.is_race_active = True
