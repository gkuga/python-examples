import time


class Decorator:
    def __init__(self, func):
        print("setting up...")
        time.sleep(1)
        self.func = func
        print("finished!")

    def __call__(self):
        print("now decorating...")
        time.sleep(1)
        self.func()
        print("decorated!")


@Decorator
def main():
    time.sleep(1)
    print("main processing")
    time.sleep(1)


main()
