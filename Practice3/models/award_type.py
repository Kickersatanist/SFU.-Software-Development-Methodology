from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class AwardType(Enum):
    Furniture = 1, "Мебель"
    Food = 2, "Еда"