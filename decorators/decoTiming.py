# Practical Example Timing

import time

# Decorator
def timed(function):
    def wrapper(*args, **kwargs):
        # gets current time then starts execution
        before = time.time()
        # executes function with args stored in value
        value = function(*args, **kwargs)
        # time after the execution
        after = time.time()
        # name of our function so we can print it
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute!")
        return value

    return wrapper


@timed
def myfunction(x):
    result = 1
    # loops thru 1-1000 and gets the range times 1
    for i in range(1, x):
        result *= i
    return result

myfunction(1000)
