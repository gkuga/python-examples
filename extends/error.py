class Base:
    def f(self):
        print("Base")


class A(Base):
    def f(self):
        print("A")
        super().f()


class B(Base):
    def f(self):
        print("B")
        super().f()


class X(A, B):
    pass


class Y(B, A):
    pass


class Z(X, Y):
    pass
