class Car:
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


my_car = Car("Toyota", "Prius", 2006)
print(my_car.get_descriptive_name())
my_car.start()
