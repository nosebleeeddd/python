# Typehinting
# Python is dynamically type language
# Only at runtime program knows types
# pip3 install mypy will allow typehinting


# :int, we can still pass any type
# mypy library will use :int as its main type 4 typehinting
def myfunction(myparameter: int):
    print(myparameter)

myfunction(10)
