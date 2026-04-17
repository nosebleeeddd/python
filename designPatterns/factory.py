# Factory Design Pattern
# good for larger projects

# WE CAN DYNAMICALLY DECIDE DURING
# RUNTIME WHETHER WE WANT TO BUILD
# THIS OR THAT.(good for on the fly)

# EXAMPLE: A person can be created
# but we want to decide whether its a teacher
# or student during runtime.

# use ABC's(abstract base class) module


from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface Method """

# Inherits the IPerson interface
class Student(IPerson):

    def __init__(self):
        self.name = "Basic Student Name"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am a teacher")


class PersonFactory:

    @staticmethod
    # what ever person gets passed this execute the method for it
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1

if __name__ == '__main__':
   choice = input("Would u like to create a student or teacher?")
# save choice to build the person in person variable
   person = PersonFactory.build_person(choice)
# full fills the IPerson contract and prints what the person is
   person.person_method()

