
#Last in First out queue
'''reverse of FIFO, this gets
the last in the queue'''


import queue

q = queue.LifoQueue()

numbers = [1,2,3,4,5,6,7]
for x in numbers:
    q.put(x)

print(q.get())
