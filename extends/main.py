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


class Base2:
    def __init__(self):
        self.x = 0


class A2(Base2):
    def __init__(self):
        super().__init__()
        self.x += 1


class B2(Base2):
    def __init__(self):
        super().__init__()
        self.x *= 2


class C(A, B):
    pass


class C2(A2, B2):
    pass


def main():
    C().f()
    c2 = C2()
    print(c2.x)


if __name__ == "__main__":
    main()
