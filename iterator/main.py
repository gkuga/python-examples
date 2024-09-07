print('--Iterable to iterator--')
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
print('--For loop to iterate through an iterable object--')
for x in mytuple:
    print(x)


class Myiterable:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        self.itr = iter(self.items)
        return self

    def __next__(self):
        return next(self.itr)


class Myiterator:
    def __init__(self, items):
        self.items = iter(items)

    def __next__(self):
        return next(self.items)


print('--Custom iterable--')
for val in Myiterable(mytuple):
    print(val)
print('--Custom iterator (call directly)--')
myiter = Myiterator(mytuple)
print(next(myiter))
print(next(myiter))
print(next(myiter))
# print(next(myiter)) # StopIteration exeption


print('--Generator--')


def mygen(items):
    for val in items:
        yield val


for val in mygen(mytuple):
    print(val)

print('--Generator (call directly)--')
mgit = mygen(mytuple)
print(next(mgit))
print(next(mgit))
print(next(mgit))
# print(next(mgit)) # StopIteration exeption
