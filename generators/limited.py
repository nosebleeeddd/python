# Generators
# Yield, lets you produces a sequence of values
# one at a time instead of computing and
# return them all at once.

# Seq 1 to 9,000,000

def mygenerator(n):
    for x in range(n):
        # returns yielded value to caller preserving local state
        yield x ** 3

values = mygenerator(9000000)

# next resumes execution after yield using preserved state
print(next(values))
