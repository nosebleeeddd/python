# Queue gets in/out data from threads

# First in first out(FIFO) queue
'''first element to enter the queue is also
first to leave the queue'''

import queue

q = queue.Queue()

numbers = [10, 20, 30, 40, 50, 60, 70]

for number in numbers:
    q.put(number)

print(q.get())
print(q.get())
