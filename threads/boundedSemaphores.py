''' How to use a BoundedSemaphore with python to limit the number
of threads running at the same time within our program.'''

# Prints 3 threads while sleeping 5 seconds after 3 prints

import threading
from time import sleep

limiter = threading.BoundedSemaphore(3)

def somefunc(id):

    limiter.acquire()
    print(f'I am thread {id}')
    sleep(5)
    limiter.release()
    return

for i in range(0,10):
    # thread executes somefunc with i as a positional argument
    t = threading.Thread(target = somefunc, args = (i,))
    t.start()

