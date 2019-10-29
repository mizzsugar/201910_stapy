import dataclasses
from typing import Iterable


@dataclasses.dataclass(frozen=True)
class Item:
    name: str
    price: int


def price(items: Iterable[Item]) -> int:
    tax_rate = 1.08
    return int(sum(item.price for item in items) * tax_rate)
