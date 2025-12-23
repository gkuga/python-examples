def main():
    class MyMeta(type):
        pass

    A = MyMeta("A", (object,), {"x": 1})
    B = MyMeta("B", (object,), {"y": 2})
    print(A, B)


if __name__ == "__main__":
    main()
