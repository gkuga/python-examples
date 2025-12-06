import dataclasses


@dataclasses.dataclass
class Example:
    shared_dict: dict[str, str] = dataclasses.field(default_factory=dict)


def main():
    example1 = Example()
    example2 = Example()

    example1.shared_dict["key1"] = "value1"
    print("example1.shared_dict:", example1.shared_dict)
    print("example2.shared_dict:", example2.shared_dict)

    example2.shared_dict["key2"] = "value2"
    print("example1.shared_dict:", example1.shared_dict)
    print("example2.shared_dict:", example2.shared_dict)

    extvars1: dict[str, str] = {}
    extvars2: dict[str, str] = {}

    extvars1["extkey1"] = "extvalue1"
    print("extvars1:", extvars1)
    print("extvars2:", extvars2)


if __name__ == "__main__":
    main()
