# Daemon threads run in the background
# this code reads in the lines in a
# text.txt file every 3 seconds.

# good for monitoring, logging, cleaning


import threading
import time


path = "text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()

        time.sleep(3)

def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()


