# Defining the base class
class MovingThing:
    def move(self):
        pass  # Base method, to be overridden by subclasses

# Defining the 'Animal' subclass
class Animal(MovingThing):
    def move(self):
        print("Walking 🐾")

# Defining the 'Car' subclass
class Car(MovingThing):
    def move(self):
        print("Driving 🚗")

# Defining the 'Plane' subclass
class Plane(MovingThing):
    def move(self):
        print("Flying ✈️")

# Testing the polymorphic behavior
moving_things = [Animal(), Car(), Plane()]

for thing in moving_things:
    thing.move()
