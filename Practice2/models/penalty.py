from dataclasses import dataclass


@dataclass(frozen=True)
class Penalty:
    id: int
    name: str
    description: str = None