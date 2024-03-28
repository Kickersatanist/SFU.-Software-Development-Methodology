from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class Difficulty(Enum):
    Easy = 1, "Легко"
    Medium = 2, "Средне"
    Hard = 3, "Тяжело"
