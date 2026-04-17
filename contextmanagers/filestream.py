# Context Managers
# Makes it easier to allocate and
# free resources the way we want.

from contextlib import contextmanager

@contextmanager
def filestream(path, mode):
    f = open(path, mode)
    yield f
    f.close()

with filestream("file.txt", "w") as file:
    file.write("Again another text")

print(file.closed)
