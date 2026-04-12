# Slow recursive way
# uses pop and pushing stack
# frames to manage function calls


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(30))
