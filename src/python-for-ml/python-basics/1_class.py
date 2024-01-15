
# A class is a blueprint for creating objects.
class Animal:
    # The __init__ method is a special method that is called when an object is created.
    def __init__(self, name, sound):
        # Attributes are variables that belong to an object.
        self.name = name
        self.sound = sound

    # Methods are functions that belong to an object.
    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

# An object is an instance of a class.
cat = Animal("Cat", "Meow")
dog = Animal("Dog", "Woof")

cat.make_sound()  # Output: Cat says Meow!
dog.make_sound()  # Output: Dog says Woof!

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
class Bird(Animal):
    def __init__(self, name, sound, can_fly):
        # Call the init method of the parent class.
        super().__init__(name, sound)
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying!")
        else:
            print(f"{self.name} can't fly.")

# Create an object of the Bird class.
penguin = Bird("Penguin", "Squawk", False)

penguin.make_sound()  # Output: Penguin says Squawk!
penguin.fly()  # Output: Penguin can't fly.


class Fish(Animal):
    def __init__(self, name, sound, can_swim):
        super().__init__(name, sound)
        self.can_swim = can_swim

    def swim(self):
        if self.can_swim:
            print(f"{self.name} is swimming!")
        else:
            print(f"{self.name} can't swim.")

# Create an object of the Fish class.
shark = Fish("Shark", "Splash", True)

shark.make_sound()  # Output: Shark says Splash!
shark.swim()  # Output: Shark is swimming!