class Dog:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print(f"{self.name} says 'Woof'!")

class Cat:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print(f"{self.name} says 'Meow'!")

class Bird:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print(f"{self.name} says 'Chirp'!")

dog = Dog("Teddy") # this isan object 
cat = Cat("Marry")
bird = Bird("Bob")

for animal in [dog, cat, bird]:
    animal.sound()


