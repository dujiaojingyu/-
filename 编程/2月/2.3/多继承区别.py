__author__ = "Narwhale"

class A(object):
    def __init__(self):
        print('A')

class B(A):
    pass
    # def __init__(self):
    #     print('B')


class C(A):
    pass

    # def __init__(self):
    #     print('C')

class D(B,C):
    pass
    # def __init__(self):
    #     print('D')

d = D()
