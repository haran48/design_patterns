class A(object):

    """ Base class """
    def __init__(self):
        print('A')

    @staticmethod
    def aa():
        print('AA')


class B(object):

    def __init__(self):
        print('B')

    @staticmethod
    def bb():
        print('BB')


class C(object):

    def __init__(self):
        print('C')

    @staticmethod
    def cc():
        print('CC')


class D(A,B,C):

    """ inherits base classes A, B and C """
    def __init__(self):
        print('D')

    def abc(self):
        self.aa()
        self.bb()
        self.cc()


a = A()
b = B()
c = C()
d = D()
d.abc()
# To check the method resolution order
order = D.__mro__
print(order)
