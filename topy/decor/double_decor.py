__author__ = 'fzhang'

#modify the behavior of a function fn
# http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@makebold
@makeitalic
def hello():
    return "hello world"

################################################################
if __name__ == "__main__":
    print hello()
    ## returns <b><i>hello world</i></b>

