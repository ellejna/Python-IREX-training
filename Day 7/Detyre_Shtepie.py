# use everything from OOP

#define a base class named DigitalSchool with the following
#print private attrinbutes: name, city, state, courses, then make the Constructor
#getter and setter for all attributes with the @property method
# methods: show_school_info returns a dictionary with school info and
# method2: organize_hackthone(): define a placeholder method to overridden by subclasses
class DigitalSchool:
    def __init__(self, name, city, state, courses):
        self.__name = name
        self.__city = city
        self.__state = state
        self.__courses = courses

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city):
        self.__city = city
    @property
    def courses(self):
        return self.__courses
    @courses.setter
    def courses(self, courses):
        self.__courses = courses
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state):
        self.__state = state

    def show_school_info(self):
        return {
            "name": self.__name,
            "city": self.__city,
            "state": self.__state,
            "courses": self.__courses,
        }
    def organize_hackthone(self):
        print("Organize a generic hackathone")
# define DS_Prishtina inheritance from Digital School superclass
# constructor where we add a new private attribute student_number
# add two more methors SCF() -> print out a specific message as "Welcome to SCF" and define organize_hackathone again
class DS_Prishtina(DigitalSchool):
    def __init__(self, name, city, state, courses, student_number):
        super().__init__(name, city, state, courses)
        self.__student_number = student_number

    @property
    def student_number(self):
        return self.__student_number
    @student_number.setter
    def student_number(self, student_number):
        self.__student_number = student_number

    def SCF(self):
        print("First edition!")
    def organize_hackthone(self):
        print("Organize a SUPER hackathone")

# If this one defines an organise_hackathone
        # it won't get the superclasses attributes, but it will be replaced with this

school = DS_Prishtina("Digital School Prishtins Pejton", "Prishtina",
                      "Kosova", ["Python", "CSS", "JS"], 100)
school.SCF()
print(school.student_number)
print(school.show_school_info())
