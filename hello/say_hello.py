import sys

__author__ = 'fzhang'


class SayHello:
    """ Hello World
    """

    def __init__(self):
        """initialise the obj"""
        pass

    def say(self, name):
        """method"""

        msg = "Hello %s" % name

        print msg

        return msg

########################################################
if __name__ == "__main__":

    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Friend"

    obj = SayHello()
    obj.say(name)
