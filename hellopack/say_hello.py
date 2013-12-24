__author__ = 'fzhang'

class SayHello:
    def __init__(self):
        pass

    def say(self, name):

        msg= "Hello %s"% name

        print msg

        return msg

if __name__ =="__main__":

    obj=SayHello()
    obj.say("Fred")