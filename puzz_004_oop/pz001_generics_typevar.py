from typing import TypeVar, Dict

K = TypeVar("K")
V = TypeVar("V")


def get_item(key: K, container: Dict[K, V]) -> V:
    return container[key]


if __name__ == "__main__":
    dict_1: Dict[str, int] = {"a": 1}
    print(get_item("a", dict_1))
