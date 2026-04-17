# Static Methods Encapsulation
# Hiding information with classes
# __ is a private attribute
# Static Methods can be called directly outside of class

 class Person:

    # Objects needs to know its self to have attributes
    def __init__(self, name, age, gender):

        self.__name = name
        self.__age = age
        self.__gender = gender

    @property                           # create a property that can be accessed
    def Name(self):
        return self.__name

    @Name.setter                        # create a setter that can be accessed
    def Name(self, value):
        self.__name = value

    # Works without objects and not related to objects
    @staticmethod
    def mymethod()
        print("Hello World!")

# StaticMethod can be called from class
Person.mymethod()


p1 = Person("Mike", 20, "m")
print(p1.Name)

# Static can be called from object, still unrelated
p1.mymethod()

p1.Name = "Bob"
print(p1.Name)
