# Practical Example for decorators
# Logging to file without logging module
# *args is positional 'tuples', **args keywords collection 'dict'

def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            # fname is the function name, in this case 'add'
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}")
        return value

    return wrapper

# DECORATING
# when we add @logged it will add the functionality to log to file
@logged
def add(x, y):
    return x + y

print(add(10, 20))
