# Hello World

import sys


def hello(thing):
    """Say hello to the thing."""
    print "Hello {}".format(thing)


def goodbye(thing):
    print "Goodbye {}".format(thing)


if __name__ == "__main__":
    user_thing = sys.argv[-1]
    sys.exit(hello(user_thing))
