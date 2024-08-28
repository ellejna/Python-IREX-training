from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.__weight = weight
        self.__height = height
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if height < 0 or height > 100:
            raise ValueError("Height must be between 0 and 100")
        self.__height = height

    @abstractmethod
    def calculate_bmi(self):
        pass
    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}, Height: {self.height}, "
              f"BMI: {self.calculate_bmi()}, Category: {self.get_bmi_category()}")

class Adult(Person):
    def calculate_bmi(self):
        return self.weight / self.height**2

    def calculate_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        elif bmi >= 30:
            return "Obese"

class Child(Person):
    def calculate_bmi(self):
        return (self.weight / self.height**2)*1.5

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal weight"
        elif 18 <= bmi < 25:
            return "Overweight"
        elif bmi < 25:
            return "Obese"

class BMIApp:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def collect_user_data(self):
        name = input("What is your name?")
        age = int(input("What is your age?"))
        weight = float(input("What is your weight in kilograms?"))
        height = float(input("What is your height in meters?"))
        if age >= 18:
            person = Adult(name, age, weight, height)
        else:
            person = Child(name, age, weight, height)
        self.people.append(person)

    def print_result(self):
        for person in self.people:
            person.print_info()
    def run(self):
        while True:
            self.collect_user_data()
            cont = input("Would you like to add another person? (y/n) ")
            self.print_result()
            if cont != "y":
                break

app = BMIApp()
app.run()
