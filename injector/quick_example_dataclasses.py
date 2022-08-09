from dataclasses import dataclass
from injector import Injector, inject


class Inner:
    def __init__(self):
        self.forty_two = 42


@inject
@dataclass
class Outer:
    inner: Inner


injector = Injector()
outer = injector.get(Outer)
print(outer.inner.forty_two)
