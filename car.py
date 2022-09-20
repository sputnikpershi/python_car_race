
"""
This module defines the Class car, which is the parent class for all car types
"""


class Car:
    """Describes a car in terms of speed and distance and uses a single method to simulate driving"""

    def __init__(self):
        self.name: str = "Generic Car"
        self.speed: float = 0
        self.distance: float = 0
        self.driving_time: float = 0
        self.speed_factor: float = 0

    def drive(self):
        """Simulates driving with a speed determined by the speed factor (to increase or decrease)"""

        # Update time and distance
        self.driving_time += 1
        self.distance = self.speed * self.driving_time

        # Update speed value according to the factor
        self.speed += self.speed_factor
