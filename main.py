
"""
This script is the main file for the car race, it initializes all the other clases
"""

# Local imports
from race import CarRace


def main():
    """Entry-point for execution"""

    # Prepare the race
    CarRace.load_cars()
    CarRace.start_race()
    CarRace.print_results()


if __name__ == '__main__':
    main()
    print("Program Completed")
