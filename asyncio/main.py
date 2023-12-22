import asyncio
import time


async def say_after(delay, what) -> str:
    print(f"say_after({delay}, {what})")
    await asyncio.sleep(delay)
    print(f"delayed {what}")
    return what


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(say_after(1, 'hello'))
        tasks.append(task1)
        task2 = tg.create_task(say_after(2, 'world'))
        tasks.append(task2)
        task3 = tg.create_task(say_after(1, 'hello-world'))
        tasks.append(task3)
        print(f"started at {time.strftime('%X')}")
    print(f"finished at {time.strftime('%X')}")
    for task in tasks:
        print(f'result: {task.result()}')

asyncio.run(main())
