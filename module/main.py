from module_a import module_name


def echo(phrase: str) -> None:
    """A dummy wrapper around print."""
    # for demonstration purposes, you can imagine that there is some
    # valuable and reusable logic inside this function
    print(phrase)


def main() -> int:
    print(f'This module name is {__name__}.')
    print(f'imported module name is {module_name()}.')
    return 0


main()
