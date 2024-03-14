from Repository import Repository
from Models import *



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