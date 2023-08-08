from module_a import module_name


def main() -> int:
    print(f'This module name is {__name__}.')
    print(f'imported module name is {module_name()}.')
    return 0


main()
