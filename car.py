
"""
This module defines the Class car, which is the parent class for all car types
"""


class Car:
    """Describes a car in terms of speed and distance and uses a single method to simulate driving"""

    def __init__(self):
        self.name: str = "Generic Car"
        self.speed: int = 0
        self.distance: int = 0
        self.driving_time: int = 0
        self.speed_factor: int = 0
        self.is_running: bool = True
        self.original_speed: int = 0

    def drive(self):
        """Simulates driving with a speed determined by the speed factor (to increase or decrease)"""

        if not self.is_running:
            return

        # Update time and distance
        self.driving_time += 1
        self.distance = self.speed * self.driving_time

        # Update speed value according to the factor
        self.speed += self.speed_factor

        # If the speed reaches 0, keep a low constant value with no decrease
        if self.speed <= 0:
            self.speed = self.original_speed
            self.speed_factor = 0
