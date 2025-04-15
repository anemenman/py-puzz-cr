from typing import Generic, Dict, TypeVar

T = TypeVar("T")


class Registry(Generic[T]):
    def __init__(self) -> None:
        self._store: Dict[str, T] = {}

    def set_item(self, k: str, v: T) -> None:
        self._store[k] = v

    def get_item(self, k: str) -> T:
        return self._store[k]

    def __str__(self):
        return str(self._store)


if __name__ == "__main__":
    auto_reg = Registry[str]()
    prices_reg = Registry[int]()

    auto_reg.set_item("honda", "civic")
    auto_reg.set_item("bmv", "x5")

    prices_reg.set_item("civic", 100000)
    prices_reg.set_item("x5", 180000)

    print(auto_reg)
    print(prices_reg)
