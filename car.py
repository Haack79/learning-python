class Vehicle:
    runs = True

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @classmethod
    def get_number_of_wheels(
        cls,
    ):  # cls is the class itself and not the instance of the class like self and is used to access class attributes and methods and shared amongst all instances of the class
        return 4

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def start(self):
        if self.runs:
            print(f"{self.get_descriptive_name()} is started. Vroom!")
        else:
            print(f"{self.get_descriptive_name()} is broken. Please fix.")


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_car = Car("Toyota", "Prius", 2006)
print(my_car.get_descriptive_name())
my_car.start()
# when we instantiate a class, we are creating an instance of that class - my_car is an instance of the Car class - my_car is an object of the Car class
# Car class inherits from the Vehicle class - Car is a child class of Vehicle - Vehicle is a parent class of Car - Car inherits all of the methods and attributes from Vehicle
# when instantiate the interpreter looks for the __init__ method and runs it - if there is no __init__ method it will look for the __init__ method in the parent class and run it
# if there is no __init__ method in the parent class it will look for the __init__ method in the grandparent class and so on
# then in the __init__ method it will look for the super() method and run it - super() will call the __init__ method of the parent class - super() is a function that returns a proxy object that delegates method calls to a parent or sibling class of type
