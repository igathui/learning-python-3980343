# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes


# Classes and Objects - Foundation for Python OOP
# Go to https://docs.python.org/3/tutorial/classes.html for more information

# Classes are user defined templates to represent real world things
# They support the principles of abstraction, encapsulation, inheritance and polymorphism

print("Defining classes and subclasses:")

class Vehicle:
    def __init__(self, chassis, wheels, doors): # The __init__ method is the class constructor. The first argument is ALWAYS "self"
        # Below we define the attributes of the class
        self.chassis = chassis
        self.wheels = wheels
        self.doors = doors

class Car(Vehicle): # Car is a subclass of Vehicle
    def __init__(self, make, model, year, color):
        # Here we call the parent class constructor and define the predefined attribute. This is called "inheritance"
        super().__init__("Car", 4, 5)
        # Below we define the attributes of this subclass. This is called "encapsulation"
        self.make = make
        self.model = model
        self.year = year
        self.color = color

class Motorcycle(Vehicle): # Motorcycle is a subclass of Vehicle
    def __init__(self, make, model, year, color, has_sidecar):
        # Here we call the parent class constructor and define the predefined attribute. This is called "inheritance"
        super().__init__("Motorcycle" , 2, 0)
        if (has_sidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        # Below we define the attributes of this subclass. This is called "encapsulation"
        self.make = make
        self.model = model
        self.year = year
        self.color = color

class Lorry(Vehicle): # Lorry is a subclass of Vehicle
    def __init__(self, make, model, year, color, capacity_tons):
        # Here we call the parent class constructor and define the predefined attribute. This is called "inheritance"
        super().__init__("Lorry", 18, 2)
        # Below we define the attributes of this subclass. This is called "encapsulation"
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.capacity_tons = capacity_tons

# Now we can create objects of these classes
print("\nCreating objects of the classes:")
car1 = Car("Toyota", "Camry", 2020, "Blue")
print(f"Car 1: {car1.year} {car1.color} {car1.make} {car1.model}")

motorcycle1 = Motorcycle("Harley-Davidson", "Street 750", 2019, "Black", False)
print(f"Motorcycle 1: {motorcycle1.year} {motorcycle1.color} {motorcycle1.make} {motorcycle1.model}")

lorry1 = Lorry("Volvo", "FH16", 2018, "White", 25)
print(f"Lorry 1: {lorry1.year} {lorry1.color} {lorry1.make} {lorry1.model}")