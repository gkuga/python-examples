import asyncio

async def task(name: str, delay: int):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished")
    return f"Result of {name}"

async def main():
    tasks = [
        asyncio.create_task(task("A", 3)),
        asyncio.create_task(task("B", 1)),
        asyncio.create_task(task("C", 2)),
    ]

    print("Waiting for tasks to complete...")
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

    print("All tasks completed!")

    for d in done:
        print(await d)

if __name__ == "__main__":
    asyncio.run(main())
