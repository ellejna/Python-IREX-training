class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    #with the age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

student1 = Student("Elena", 17)
student2 = Student("Agon", 18)
print(student1.age)
print(student2.age)
