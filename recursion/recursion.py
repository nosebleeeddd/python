# Recursion,
# technique of function calling itself


n = 7

factorial = 1
while n > 0:
    factorial = factorial * n
    n -= 1

print(factorial)

def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number
