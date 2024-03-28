from datetime import datetime

from models.award import Award
from models.difficulty import Difficulty
from models.penalty import Penalty
from models.user import User


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
