# Infinite Sequences waste no memory
# dont have to set a limit
# we just print the next values till we run out of memory

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()

#print(next(values))
#print(next(values))
#print(next(values))
#print(next(values))
#print(next(values))

# INSTEAD OF PRINTING SINGLES
# USE A FOR RANGE LOOP

for x in range(1, 6):
    print(next(values))
