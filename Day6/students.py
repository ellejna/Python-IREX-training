class Klasa:
    def training(self):
        pass
class Student(Klasa):
    def __init__(self, name, gjuhaprogramuse):
        self.name = name
        self.gjuhaprogramuse = gjuhaprogramuse
    def traning(self, gjuhaprogramuse):
        return self.gjuhaprogramuse

class Teacher(Klasa):
    def __init__(self, name, gjuhaprogramuse, level):
        self.name = name
        self.gjuhaprogramuse = gjuhaprogramuse
        self.level = level
    def training(self):
        return self.gjuhaprogramuse
    def level(self):
        return self.level

Alma = Teacher('Alma', ["html", "css", "python"], "advanced")
Olta = Student('Olta', ["java", "react", "python"])
print("Alma: ")
print(Alma.training())
print("Olta: ")
print(Olta.traning())