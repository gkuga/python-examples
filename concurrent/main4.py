from time import sleep
from concurrent.futures import ThreadPoolExecutor
from functools import partial


def func(i):
    sleep(1)
    if i == 2:
        raise "error"
    print(f"{i}\n", flush=True, end="")


print('通常')
with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(5):
        executor.submit(
            func, i
        )


print('迷走＆失敗')  # https://qiita.com/ninomiyt/items/b2546806847e199a3a9b
with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(5):
        executor.submit(
            lambda: func(i)
        )


print('迷走2')
with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(5):
        executor.submit(
            lambda num: func(num), i
        )


print('迷走3')
with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(5):
        executor.submit(
            lambda num=i: func(num)
        )


print('迷走4')
with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(5):
        executor.submit(
            partial(func, i)
        )

print('迷走4&result()')
with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(5):
        executor.submit(
            partial(func, i)
        ).result()
