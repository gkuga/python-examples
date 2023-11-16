from abc import ABCMeta, abstractmethod


class BaseFoo(metaclass=ABCMeta):
    @property
    @abstractmethod
    def x(self) -> str:
        raise NotImplementedError


class FooWithError(BaseFoo):
    pass


class Foo(BaseFoo):
    x = 'foo'

    @classmethod
    def y(cls) -> str:
        print(cls.x)

    @staticmethod
    def z() -> str:
        print(Foo.x)


try:
    foo = FooWithError()
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")

print(FooWithError.x)
print(FooWithError.x())
