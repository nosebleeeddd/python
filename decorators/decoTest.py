# Decorators wrap functions with additional
#functionality

# Inside of wrapper we pass *args, **kwargs so we can use function
#with any parameters inside , like hello.
#DECORATORS DONT APPLY TO
#PARAMETERS AUTOMATICALLY!

def mydecorator(function):

    def wrapper(*args, **kwargs):
         print("i am decorating your function!")
         function(*args, **kwargs)                                 # runs hello_word func

        # return another function that calls initial func with decorated code
    return wrapper



# wrap the function with decorator then call function'
# mydecorator runs once, hello becomes wrapper, hello runs wrapper
@mydecorator
def hello(person):
    print(f"hello {person}!")

hello("Nate")



