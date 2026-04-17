# Singleton Design Pattern
# one of many methods to implement a singleton

# These are classes that only have one single instance
# Ensure that only one object instance exists

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data():
        """ Implement in child class """

# Inherit from the IPerson interface
class PersonSingleton(IPerson):

    # single instance we create
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            # create person if empty
            PersonSingleton("Default Name", 0)
        # return instance we had previously
        return PersonSingleton.__instance

    # initializer
    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    # Gets the data
    @staticmethod
    def print_data():
        print(f"name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")

# Creates single instance
p = PersonSingleton("Mike", 30)
print(p)                                    # prints object memory address
p.print_data()

# Gets the same instance , doesnt create a second instance
p2 = PersonSingleton.get_instance()
print(p2)
p.print_data()
