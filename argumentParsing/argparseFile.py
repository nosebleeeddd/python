# Argument parsing with files

# w+ opens a file for both writing and reading
# if file exists replace content, if not create
# file with content

import sys

# Usage: main.py <filename> <message for file>

filename = sys.argv[1]
message = sys.argv[2]

# len() to add conditionals to args

with open(filename, 'w+') as f:
    f.write(message)
