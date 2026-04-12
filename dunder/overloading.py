# Overloading Adding Dunders

'''Python doesnt know how to add two custom
objects by default. For a custom class like
vector, this __add__ method doesnt exist so we define it.'''

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    #def __str__ , u can modify what happens when we typecast the vec to a str
    # instead type casting vector we can modify how we can represent it
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"


    # this always returns 10 when printing len of vector
    def __len__(self)_:
        return 10

    # modifys the call output v3()
    def __call__(self):
        print("I was called")

v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2

print(v3.x)
print(v3.y)

print(v3)

print(len(v3))

v3()
