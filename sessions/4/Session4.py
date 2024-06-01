# Classes Objects and methods
# Class is a blueprint for creating objects
# Objects are instances of classes

# Class definition
# class Car:
#     ...

# Instance methods and variables
class Car:
    # A class variable
    # A class is accessible through the class name or an object.
    number_of_cars = 0

    # A paramaterized constructor
    def __init__(self, make, model, year=2000, color="Black"):
        # Instance variables
        # An instance is accessible through the instance/object name.
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_level = 0

        # Private variable
        self.__password = "1234"

        # Increment the number of cars
        Car.number_of_cars += 1 # == Car.number_of_cars = Car.number_of_cars + 1

    # A method
    # 0, 1, 2, 3, 4 
    def drive(self):
        if self.fuel_level >= 1:
            self.fuel_level -= 1
            print("Driving the car")
        else:
            print("Sorry you don't have enough fuel.")
            self.stop()

    # A method
    def fuel(self, fuel):
        self.fuel_level += fuel
        print(f"Filling the car with {fuel} liters of fuel") # f-string
        # print("Filling the car with {} liters of fuel".format(fuel)) # string formatting - Same output as above

    def stop(self):
        print("Stopping the car")

    # Destructor method
    def __del__(self):
        Car.number_of_cars -= 1
        print("Deleting the car")

    @classmethod
    def reset_number_of_cars(cls):
        cls.number_of_cars = 0

    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.color}"
    
    def __repr__(self):
        return f"{self.make} {self.color}"
    

toyota = Car("Toyota", "Some Model", 2017, "Blue")
# toyota.drive()
# toyota.fuel(5)
# toyota.drive()
# toyota.drive()
# toyota.drive()
# toyota.drive()
# toyota.drive()
# toyota.drive()

# del toyota
Car.reset_number_of_cars()
print(toyota)

# print(Car.number_of_cars)

        
# print("Initial number of cars: ", Car.number_of_cars)

# tesla = Car("Tesla", "Model X", 2021, "Red")
# unkown = Car("Unknown", "Unknown")

# print(tesla.number_of_cars)
# print("Final number of cars: ", unkown.number_of_cars)

# print("Unknown car color is: ", unkown.color)
# print(tesla.model)
# print(Car.number_of_cars)
# print(tesla.__password)


