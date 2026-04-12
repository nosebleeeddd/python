# Iterating is faster than recursion
# recursion requires popping and pushing
# stack frames.


def fibonacci(n):
    a, b = 0, 1
    for x in range(n-1):        # -1 gets prev position
        a, b = b, a+b           # change to n for index number
    return a

print(fibonacci(3))


