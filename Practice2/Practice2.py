from datetime import datetime
from enum import Enum


class User:
    def __init__(self, id: int, name: str, level: int = 0, awards: int = 0, countHabits: int = 0):
        self.id = id
        self.name = name
        self.level = level
        self.awards = awards
        self.countHabits = countHabits

    def __str__(self):
        return f'\nПользователь: {self.id} - {self.name} - {self.level} - {self.awards} - {self.countHabits}'

    # Используется для dict
    def __repr__(self):
        return self.__str__()


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
                 enddate: datetime, periodicity: datetime.day, startdate: datetime = datetime.now().date()):
        self.id = id
        self.name = name
        self.difficulty = difficulty
        self.penalty = penalty
        self.award = award
        self.startdate = startdate
        self.enddate = enddate
        self.periodicity = periodicity
        self.user = user

    def __str__(self):
        return (f'\nПривычка: {self.id} - {self.name} - {self.difficulty.value[1]} - {self.penalty} - {self.award} - {self.startdate},'
                f'{self.enddate} - {self.periodicity} дней - {self.user}')

    def __repr__(self):
        return self.__str__()


class Repository:
    __users = {}
    __awards = {}
    __habits = {}

    @staticmethod
    def addUser(user: User):
        if user.id not in Repository.__users.keys():
            Repository.__users[user.id] = user
        else:
            raise Exception(f"ID: {user.id} уже имеется в пользователях")

    @staticmethod
    def getUser(id):
        if id in Repository.__users.keys():
            return Repository.__users.get(id)

    @staticmethod
    def getUsers():
        return Repository.__users


    @staticmethod
    def addAward(award: Award):
        if award.id not in Repository.__awards.keys():
            Repository.__awards[award.id] = award
        else:
            raise Exception(f"ID: {award.id} уже имеется в наградах")
    @staticmethod
    def getAward(id):
        if id in Repository.__awards.keys():
            return Repository.__awards.get(id)
    @staticmethod
    def getAwards():
        return Repository.__awards

    @staticmethod
    def addHabit(habit: Habit):
        if habit.id not in Repository.__habits.keys():
            Repository.__habits[habit.id] = habit
        else:
            raise Exception(f"ID: {habit.id} уже имеется в привычках")

    @staticmethod
    def getHabit(id):
        if id in Repository.__habits.keys():
            return Repository.__habits.get(id)

    @staticmethod
    def getHabits():
        return Repository.__habits


Repository.addUser(User(len(Repository.getUsers()) + 1, "Pavel"))
Repository.addUser(User(len(Repository.getUsers()) + 1, "Alina"))
Repository.addUser(User(len(Repository.getUsers()) + 1, "Yana"))
Repository.addAward(Award(len(Repository.getAwards()) + 1, "Мороженое", Type.Food))
Repository.addAward(Award(len(Repository.getAwards()) + 1, "Кровать", Type.Furniture))
Repository.addHabit(Habit(len(Repository.getHabits()) + 1, "Умываться по утрам", Difficulty.Easy, "Прибраться"
                          ,Repository.getUser(1),Repository.getAward(1),"2024-31-03", "7"))
print(f'Первая привычка: {Repository.getHabit(1)}')
print(f'\nПервая награда: {Repository.getAward(1)}')
print(f'\nСписок пользователей: {Repository.getUsers()}')