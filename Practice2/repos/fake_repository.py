from models.award import Award
from models.habit import Habit
from models.user import User
from repos.repository import Repository


class FakeRepository(Repository):
    __users = {}
    __awards = {}
    __habits = {}

    @staticmethod
    def add_user(self, user: User):
        if user.id not in Repository.__users.keys():
            FakeRepository.__users[user.id] = user
        else:
            raise Exception(f"ID: {user.id} уже имеется в пользователях")

    @staticmethod
    def get_user(self, id):
        if id in FakeRepository.__users.keys():
            return FakeRepository.__users.get(id)

    @staticmethod
    def get_users():
        return Repository.__users

    @staticmethod
    def add_award(self, award: Award):
        if award.id not in Repository.__awards.keys():
            Repository.__awards[award.id] = award
        else:
            raise Exception(f"ID: {award.id} уже имеется в наградах")

    @staticmethod
    def get_award(self, id):
        if id in Repository.__awards.keys():
            return Repository.__awards.get(id)

    @staticmethod
    def get_awards(self):
        return Repository.__awards

    @staticmethod
    def add_habit(self, habit: Habit):
        if habit.id not in Repository.__habits.keys():
            Repository.__habits[habit.id] = habit
        else:
            raise Exception(f"ID: {habit.id} уже имеется в привычках")

    @staticmethod
    def get_habit(self, id):
        if id in Repository.__habits.keys():
            return Repository.__habits.get(id)

    @staticmethod
    def get_habits(self):
        return Repository.__habits
