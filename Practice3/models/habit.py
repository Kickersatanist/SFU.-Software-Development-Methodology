from datetime import datetime

from modelsOLD.award import Award
from modelsOLD.difficulty import Difficulty
from modelsOLD.penalty import Penalty
from modelsOLD.user import User


class Habit:
    id = id
    name: str
    difficulty: Difficulty
    penalty: Penalty
    award: Award
    start_date: datetime = datetime.now().date()
    end_date: datetime
    periodicityDay: datetime.day = None
    periodicityHour: int = None
    user: User
    is_done: bool
