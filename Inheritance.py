class Pets(object):

    """ create a base class """
    def __init__(self, name, activity):
        self.name = name
        self.activity = activity

    def get_name(self):
        return self.name

    def get_activity(self):
        return self.activity

    """ use dudder str to format the returned value """
    def __str__(self):
        return "The pet %s %s" % (self.name, self.activity)


class Dog(Pets):

    """ Method Overloading with different arguments """
    def __init__(self, name, activity, chase):
        super().__init__(name, activity)
        self.chase = chase

    def chases(self):
        return self.chase

    """ Method Overriding by adding a different implementation of the super class"""
    def __str__(self):
        if self.chase == 'Cat':
            return super().__str__() + " and chases %s" % self.chase


p = Pets('Dog', 'Barks')
print(p)
d = Dog('Dog', 'Barks', 'Cat')
print(d)
# to check the base classes
ck1 = Dog.__bases__
print(ck1)
# to check the sub classes - This is a list
ck2 = Pets.__subclasses__()
print(ck2)

