import datetime
import unittest

from models.award import Award
from models.award_type import AwardType
from models.difficulty import Difficulty
from models.habit import Habit
from models.penalty import Penalty
from models.user import User
from services import user_service


class UserServiceTest(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "Pavel")
        self.award = Award(1, "Мороженое", AwardType.Food)
        self.user_habit_done = Habit()
        self.user_habit_done.id = 1
        self.user_habit_done.name = "Умываться по утрам"
        self.user_habit_done.difficulty = Difficulty.Easy
        self.user_habit_done.penalty = Penalty(1, "Убраться", "Нужно будет сделать генеральную уборку")
        self.user_habit_done.award = self.award
        self.user_habit_done.end_date = datetime.datetime.now() + datetime.timedelta(days=7)
        self.user_habit_done.user = self.user
        self.user_habit_done.is_done = True

        self.user_habit_not_done = Habit()
        self.user_habit_not_done.id = 1
        self.user_habit_not_done.name = "Чистить зубы по вечерам"
        self.user_habit_not_done.difficulty = Difficulty.Easy
        self.user_habit_not_done.penalty = Penalty(1, "Выучить стих", "Нужно будет выучить 8-ми строчный стишок")
        self.user_habit_not_done.award = self.award
        self.user_habit_not_done.end_date = datetime.datetime.now() + datetime.timedelta(days=7)
        self.user_habit_not_done.user = self.user
        self.user_habit_not_done.is_done = False

        self.habits = [self.user_habit_done, self.user_habit_not_done]

    def test_calculate_lvl(self):
        # count_habits = len([habit for habit in self.habits if habit.user == self.user])
        self.assertEqual(user_service.calculate_lvl(self.user, [self.user_habit_done, self.user_habit_not_done]), 1,
                         "Неправильный уровень у пользователя.")

    def test_calculate_awards(self):
        self.assertEqual(user_service.calculate_awards(self.user, [self.user_habit_done, self.user_habit_not_done]), 1,
                         "Неправильное количество наград у пользователя.")

    def test_calculate_habits(self):
        self.assertEqual(user_service.calculate_habits(self.user, [self.user_habit_done, self.user_habit_not_done]), 2,
                         "Неправильное количество привычек у пользователя.")

    def test_get_user_awards(self):
        user_awards = [habit.award for habit in self.habits if habit.user == self.user and habit.is_done]
        self.assertEqual(user_service.get_user_awards(self.user, [self.user_habit_done, self.user_habit_not_done]),
                         user_awards, "Неправильные значения наград у пользователя.")
