from dataclasses import dataclass
from datetime import datetime
from enum import Enum


@dataclass(frozen=True)
class User:
    # def __init__(self, id: int, name: str, level: int = 0, awards: int = 0, countHabits: int = 0):
    #     self.id = id
    #     self.name = name
    #     self.level = level
    #     self.awards = awards
    #     self.countHabits = countHabits
    id: int
    name: str
    level: int = 0
    countAwards: int = 0
    countHabits: int = 0

    # def __str__(self):
    #     return f'\nПользователь: {self.id} - {self.name} - {self.level} - {self.awards} - {self.countHabits}'
    #
    # # Используется для dict
    # def __repr__(self):
    #     return self.__str__()


class Difficulty(Enum):
    Easy = 1, "Легко"
    Medium = 2, "Средне"
    Hard = 3, "Тяжело"


class Type(Enum):
    Furniture = 1, "Мебель"
    Food = 2, "Еда"


class Award:
    def __init__(self, id: int, name: str, type: Type):
        self.id = id
        self.name = name
        self.type = type

    def __str__(self):
        return f'\nНаграда: {self.id} - {self.name} - {self.type.value[1]}'

    def __repr__(self):
        return self.__str__()


class Habit:
    def __init__(self, id: int, name: str, difficulty: Difficulty, penalty: str, user: User, award: Award,
                 enddate: datetime, startdate: datetime = datetime.now().date(), periodicityDay: datetime.day = None,
                 peridocityHour: int = None):
        self.id = id
        self.name = name
        self.difficulty = difficulty
        self.penalty = penalty
        self.award = award
        self.startdate = startdate
        self.enddate = enddate
        self.periodicityDay = periodicityDay
        self.periodicityHour = peridocityHour
        self.user = user

    def __str__(self):
        if self.periodicityDay is not None:
            return (
                f'\nПривычка: {self.id} - {self.name} - {self.difficulty.value[1]} - {self.penalty} - {self.award} - {self.startdate},'
                f'{self.enddate} - раз в {self.periodicityDay} дней - {self.user}')
        elif self.periodicityHour is not None:
            return (
                f'\nПривычка: {self.id} - {self.name} - {self.difficulty.value[1]} - {self.penalty} - {self.award} - {self.startdate},'
                f'{self.enddate} - раз в {self.periodicityHour} ч. - {self.user}')

    def __repr__(self):
        return self.__str__()
