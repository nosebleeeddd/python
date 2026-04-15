import argparse
import time

parser = argparse.ArgumentParser()

# our argv[1] is stored in greeting
parser.add_argument('greeting', help='The greeting message displays')

# we can also use flags -,
#nargs is number of args required
parser.add_argument('-n', '--numbers', type=float, nargs=2, help='The numbers to be added')

# Adding verbose flag
parser.add_argument('-v', '--verbosity', type=int, choices=[0,1,2], help='Determines how much info is displayed')

# Boolean Flag
parser.add_argument('--debug', action='store_true', help='Enables debug mode')


args = parser.parse_args()

# Start the time measurement for debug
if args.debug:
    start = time.perf_counter()


# Prints all arguments that were passed successfully
print(args)
# Prints the argument passed + stored in argument
print(args.greeting)
# Prints the two numbers when passed successfully
print(args.numbers)


# verbosity for displaying more or less info

if args.verbosity is None:
    print(args.greeting)
    if args.numbers is not None:
        print(sum(args.numbers))

else:
    if args.verbosity >= 0:
        print(args.greeting)
        if args.numbers is not None:
            print(sum(args.numbers))
    if args.verbosity >= 1:
        print(args.numbers)
    if args.verbosity == 2:
        print('Extra Info')

# End the time measurement for debug
if args.debug:
    end = time.perf_counter()
    print(end - start)

