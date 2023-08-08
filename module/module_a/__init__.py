import module_b


def module_name() -> str:
    print(module_b.module_name())
    return(__name__)
