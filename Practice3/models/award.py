from dataclasses import dataclass

from modelsOLD.award_type import AwardType


@dataclass(frozen=True)
class Award:
    id: int
    name: str
    type: AwardType
