
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
    finished_cars: List[Car] = []
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
            speed: int = randint(config.speed_range_consumer_car[0], config.speed_range_consumer_car[1])
            consumer_car.speed = speed
            consumer_car.original_speed = speed
            consumer_car.speed_factor = -decay_value
            consumer_car.name = f"consumer_car{index + 1}"
            CarRace.cars.append(consumer_car)

        # Create the "Sport" (fast) cars
        for index in range(config.number_of_sport_cars):
            sport_car: Car = Car()
            increase_value = randint(config.speed_increase_range[0], config.speed_increase_range[1])
            speed: int = randint(config.speed_range_sport_car[0], config.speed_range_sport_car[1])
            sport_car.speed = speed
            sport_car.original_speed = speed
            sport_car.speed_factor = increase_value
            sport_car.name = f"sport_car{index + 1}"
            CarRace.cars.append(sport_car)

        CarRace.is_race_active = True
        CarRace.number_of_cars = len(CarRace.cars)

    @staticmethod
    def start_race():
        """Allow each car to drive until all of them cross the finish line"""

        cars_race_state: List[bool] = [True for _ in range(CarRace.number_of_cars)]

        while CarRace.is_race_active:
            CarRace.number_of_seconds += 1
            print(f"\n===== Race duration: {CarRace.number_of_seconds} secs =====")

            # Drive each, check if it has reached the goal
            for car_index in range(CarRace.number_of_cars):
                current_car: Car = CarRace.cars[car_index]
                if not current_car.is_running:
                    continue
                current_car.drive()
                print(f"- car: {current_car.name} has distance: {current_car.distance}")

                if current_car.distance >= config.max_distance:
                    print(f"- car: {current_car.name} has crossed the line!")
                    current_car.is_running = False
                    cars_race_state[car_index] = False
                    CarRace.finished_cars.append(current_car)

            CarRace.is_race_active = any(cars_race_state)

    @staticmethod
    def print_results():
        """Print a formatted summary of the race results """

        # Print header results
        print("\n\n====== RACE RESULTS! ======")
        print(f"Race duration: {CarRace.number_of_seconds} seconds")
        print(f"Race distance: {config.max_distance} mts")
        print(f"Car ranking ({CarRace.number_of_cars} cars): ")

        # Arrange cars by arrival
        rank_index: int = 0

        for car in CarRace.finished_cars:
            rank_index += 1
            print(f"- #{rank_index}: {car.name}, race time: {car.driving_time}")
