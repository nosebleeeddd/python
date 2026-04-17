# Proxy Design Pattern
# Gives you more encapsulation
# Controls access to another object
# without changing the original object


from abc import ABCMeta, abstractstaticmethod

# Create our interface
class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface Method """

# Class inherits our interface method
class Person(IPerson):

    def person_method(self):
        print("I am a person")

# Proxy or Middle man create and handles the person object
class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am the proxy functionality")
        self.person.person_method()

p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()
