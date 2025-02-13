# Define a base class for a Car
class Car:
    def __init__(self, make, model, year):
        # Encapsulation: Use private attributes
        self._make = make
        self._model = model
        self._year = year
        self._mileage = 0  # Default mileage

    # Getter methods (encapsulation)
    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_mileage(self):
        return self._mileage

    # Setter method for mileage
    def set_mileage(self, mileage):
        if mileage >= 0:
            self._mileage = mileage
        else:
            print("Mileage cannot be negative.")

    # Method to display car details
    def display_info(self):
        print(f"Car: {self._year} {self._make} {self._model}")
        print(f"Mileage: {self._mileage} miles")

    # Method to simulate driving the car
    def drive(self, miles):
        if miles > 0:
            self._mileage += miles
            print(f"Driven {miles} miles. Total mileage: {self._mileage} miles.")
        else:
            print("Miles driven must be positive.")


# Define a subclass for ElectricCar (inheritance)
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)  # Call the parent class constructor
        self._battery_capacity = battery_capacity  # Additional attribute for ElectricCar

    # Override the display_info method
    def display_info(self):
        super().display_info()  # Call the parent class method
        print(f"Battery Capacity: {self._battery_capacity} kWh")

    # Method specific to ElectricCar
    def charge_battery(self):
        print(f"Charging the {self._make} {self._model} battery...")


# Main program
if __name__ == "__main__":
    # Create an instance of Car
    my_car = Car("Toyota", "Corolla", 2020)
    my_car.drive(100)
    my_car.display_info()

    print("\n")

    # Create an instance of ElectricCar
    my_electric_car = ElectricCar("Tesla", "Model S", 2023, 100)
    my_electric_car.drive(50)
    my_electric_car.charge_battery()
    my_electric_car.display_info()