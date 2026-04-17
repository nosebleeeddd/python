# Encapsulation
# Hiding information with classes
# __ is a private attribute
# With your setter you have control over your class

 class Person:

    def __init__(self, name, age, gender):

        self.__name = name
        self.__age = age
        self.__gender = gender

    @property                           # create a property that can be accessed
    def Name(self):
        return self.__name

    @Name.setter                        # create a setter that can be accessed
    def Name(self, value):
        # we can add constraints for the setter
        if value == "Bob":
            self.__name = "Default Name"
        else:
            self.__name = value

p1 = Person("Mike", 20, "m")
print(p1.Name)

p1.Name = "Bob"
print(p1.Name)
