from typing import Optional


def greet(name: Optional[str]) -> str:
    return f"Helo, {name if name is not None else 'world'}!"


print(greet())
