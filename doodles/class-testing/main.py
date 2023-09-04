
class Car():
    """Simple Car class."""
    def __init__(self, make, model, year):
        """Initialise car attributes."""
        self.make = make
        self.model = model
        self.year = year

        # Fuel capacity and leve in liters
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("The gas tank is full!")

    def drive_car(self):
        """Driving the car."""
        print("The car is moving.")

# Create object
my_summer_car = Car("Mitsubishi", "Lancer", "2002")

# Access some attribute values
print(my_summer_car.make)
print(my_summer_car.year)

# Call some methods
my_summer_car.drive_car()
my_summer_car.fill_tank()

# Modify some attribute values
my_new_car = Car("Opel", "Insignia", "2021")
my_new_car.fuel_level = 5

# Create method to modify some attributes
