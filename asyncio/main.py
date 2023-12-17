import asyncio
import time


async def say_after(delay, what) -> str:
    await asyncio.sleep(delay)
    print(what)
    return what


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(say_after(1, 'hello'))
        tasks.append(task1)
        task2 = tg.create_task(say_after(2, 'world'))
        tasks.append(task2)
        # print(task1.result(), task2.result())
        print(f"started at {time.strftime('%X')}")
    print(f"finished at {time.strftime('%X')}")
    for task in tasks:
        print(f'result: {task.result()}')

asyncio.run(main())
