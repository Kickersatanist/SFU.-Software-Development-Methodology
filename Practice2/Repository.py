from Models import *
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