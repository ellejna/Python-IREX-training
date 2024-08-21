class Training:
    def __init__(self, name):
        self.name = name

class Student(Training):
    def findRole(self, name, age, training):
        self.name = name
        self.age = age
        self.training = training

student1 = Student('Bob', 25, True)
student2 = Student('Janice', 20, False)
student3 = Student('Jeff', 23, True)

for student in [student1, student2, student3]:
    print(student.name, student.age, student.training)