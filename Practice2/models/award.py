from dataclasses import dataclass

from models.award_type import AwardType


@dataclass(frozen=True)
class Award:
    id: int
    name: str
    type: AwardType
