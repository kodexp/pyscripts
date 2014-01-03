# file:  class_decorator.py
def method_decorator(fn):
    "Example of a method decorator"
    def decorator(*args, **kwargs):
        print "\tInside the decorator"
        return fn(*args, **kwargs)

    return decorator


def class_decorator(*method_names):
    def class_rebuilder(cls):
        "The class decorator example"
        class NewClass(cls):
            "This is the overwritten class"
            def __getattribute__(self, attr_name):


                obj = super(NewClass , self).__getattribute__(attr_name)

                if hasattr(obj, '__call__') and attr_name in method_names:
                    return method_decorator(obj)    # do decorate
                return obj  # not decorated

        return NewClass
    return class_rebuilder


@class_decorator('first_method', 'second_method')
class MySecondClass(object):
    """
    This class is decorated
    """
    def first_method(self, *args, **kwargs):
        print "\t\tthis is a the MySecondClass.first_method"

    def second_method(self, *args, **kwargs):
        print "\t\tthis is the MySecondClass.second_method"

if __name__ == "__main__":
    print "::: With a decorated class :::"
    z = MySecondClass()
    z.first_method()
    z.second_method()

