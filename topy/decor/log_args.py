__author__ = 'fzhang'

# @ aspect-oriented programming

def logger(func):
    """
    A decorator to modify the behavior of func in the inner function
    """
    def inner(*args, **kwargs): #1
        print "Arguments were: %s, %s" % (args, kwargs)
        return func(*args, **kwargs) #2

    return inner

@logger
def add(x,y):
    return (x+y)

@logger
def foo(x, y=2):
    return x/y


if __name__ =="__main__":

    print add(1,1)

    print foo(2,y=1)