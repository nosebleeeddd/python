# Typehinting
# After installing mypy lib
# Return values can also be typehinted

# we type hint the return value with an ->
def myfunction(myparameter: int) -> str:
    return f"{myparameter + 10}"

# we exepect a string here
def otherfunction(otherparameter: str)
    print(otherparameter)

otherfunction(myfunction(10))

# we can also type hint a list of types
def dosth(param: list[int])
