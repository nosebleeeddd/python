#Magic methods or dunders(Double underscore)methods

#Dunders have a certain special type that executes



class Person:

    # Constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age


    # Destructor, 'python deletes automatically'
    def __del__(self):
        print("Object is being deconstructed")


p = Person("Mike", 25)

# del p                     # this is so you can manually delete
