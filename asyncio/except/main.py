import asyncio


async def task1():
    await asyncio.sleep(1)
    raise ValueError("Task 1 failed")


async def task2():
    await asyncio.sleep(2)
    raise KeyError("Task 2 failed")


async def task3():
    await asyncio.sleep(3)
    print("Task 3 completed")


async def task4():
    try:
        await asyncio.sleep(4)
        print("Task 4 completed")
    except asyncio.CancelledError:
        print("Task 4 was cancelled")
        raise


async def run_tasks():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(task1())
            tg.create_task(task2())
            tg.create_task(task3())
            tg.create_task(task4())
    except* Exception as eg:
        print(f"Caught {len(eg.exceptions)} exceptions")
        for exc in eg.exceptions:
            print(f"  - {type(exc).__name__}: {exc}")


def main():
    asyncio.run(run_tasks())


if __name__ == "__main__":
    main()
