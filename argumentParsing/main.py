# Argument parsing with getopt
# this will allow us to set -flags
# as validation for arguments

import sys
import getopt

# if file is ran and no args are provided we run a default instead of error
filename = "default.txt"
message = "Default message"


# gets every string after the filename
# -f -o are flags/keyValuePairs with filename and message
opts, args = getopt.getopt(sys.argv[1:], "f:o:", ['filename', 'message'])


for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, 'w+') as f:
    f.write(message)
