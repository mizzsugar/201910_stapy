import dataclasses
from typing import Iterable


@dataclasses.dataclass(frozen=True)
class Item:
    name: str
    price: int


def price(items: Iterable[Item], eat_in: bool) -> int:
    tax_rate = 1.10 if eat_in else 1.08
    return int(sum(item.price for item in items) * tax_rate)
