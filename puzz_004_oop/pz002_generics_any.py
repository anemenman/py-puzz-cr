from typing import List, Any


def first(container: List[Any]) -> Any:
    return container[0]


if __name__ == "__main__":
    list_1: List[str] = ["one", "two", "three"]
    print(first(list_1))

    list_2: List[int] = [1, 2, 3]
    print(first(list_2))
