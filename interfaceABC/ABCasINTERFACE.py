# Abstract Classes define the input and
# output of something, and provide an
# implementation.

# Interfaces define the input and output
# of something, they do not specify implementation.
# To use abstract classes or implement interfaces
# u need a regular class that inherits from an abstract class.

from abc import ABC, abstractmethod

# ABSTRACT CLASS INHERITING ABC
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def walk(self):
    print(f'{self.name} is walking')

# ABSTRACTED USED AS AN INTERFACE must have @abstractmethod
class Talking(ABC):
    @abstractmethod
    def talk(self):
        pass


# CONCRETE CLASS THAT INHERITS FROM ANIMAL
class Dog(Animal):
    def __init__(self, name):
        # calls the constructor of the super class which is Animal
        super().__init__(name)

    # Dog has its own function and inherits from animal
    def wag_tail(self):
    print(f'{self.name} is wagging tail')


#INTERFACE
class Talking(Dog, Talking):
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print(f'{self.name} is barking')


if __name__ = '__main__':
    pluto = Dog('Pluto')
    pluto.walk()
    pluto.wag_tail()

    # Instantiate dog interface that can use all
    goofy = Talking('Goofy')
    goofy.walk()
    goofy.wag_tail()
    goofy.talk()



# BECAUSE EVERY ANIMAL TALKS DIFFERENTLY
# WE HAVE TO IMPLEMENT IT AS AN INTERFACE
