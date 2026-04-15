# More Generators

import sys

def mygenerator(n):
    for x in range(n):
        yield x ** 3

values = mygenerator(5)
# the bytes dont change with generator size, we just state a limit
print(sys.getsizeof(values))

#for x in values:
#    print(x)

