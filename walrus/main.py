print('--Basic assignment expression--')
# := assigns a value and evaluates to that value in the same expression
x = 5
if (y := x * 2) > 5:
    print(f'y is {y}, which is greater than 5')


print('--Without walrus (traditional style)--')
data = [1, 2, 3, 4, 5]
n = len(data)
if n > 3:
    print(f'there are {n} items')


print('--With walrus--')
if (n := len(data)) > 3:
    print(f'there are {n} items')
# n is still available outside the if block
print(f'n is still accessible outside the block: n = {n}')


print('--while loop (common pattern for reading until a sentinel)--')
values = iter([10, 20, 30, 0, 40])


def fake_input():
    return next(values)


while (chunk := fake_input()) != 0:
    print(f'received: {chunk}')
print('received 0, stopping')


print('--Reusing a computed value inside a list comprehension--')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Without walrus, you'd have to compute x * x twice, or use a helper function
squares_over_20 = [y for x in numbers if (y := x * x) > 20]
print(f'squares greater than 20: {squares_over_20}')


print('--Using a regex match result directly in a condition--')
import re

texts = ['abc123', 'no-digits-here', 'xyz789']
for text in texts:
    if (m := re.search(r'\d+', text)) is not None:
        print(f'{text!r} contains digits: {m.group()}')
    else:
        print(f'{text!r} has no digits')


print('--Avoiding a duplicate call in a filter + transform comprehension--')


def slow_square(n):
    print(f'  computing slow_square({n})...')
    return n * n


# Without walrus, slow_square would be called twice per element:
# result = [slow_square(x) for x in range(5) if slow_square(x) > 4]

# With walrus, it's called only once
result = [square for x in range(5) if (square := slow_square(x)) > 4]
print(f'result: {result}')
