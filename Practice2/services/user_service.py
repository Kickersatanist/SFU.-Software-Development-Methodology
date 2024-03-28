from models.user import User


def calculate_lvl(user: User, habits) -> int:
    count_habits = 0
    for habit in habits:
        if habit.user == user:
            count_habits += 1

    if count_habits < 0:
        raise Exception("Количество привычек ниже нуля.")
    elif 0 <= count_habits < 5:
        return 1
    elif 5 <= count_habits < 10:
        return 2
    else:
        raise Exception("Новые уровни еще не добавлены!")


def calculate_awards(user: User, habits) -> int:
    count_awards = 0
    for habit in habits:
        if habit.is_done and habit.user == user:
            count_awards += 1

    if count_awards < 0:
        raise Exception("Количество наград ниже нуля.")
    elif 0 <= count_awards < 5:
        return 1
    elif 5 <= count_awards < 10:
        return 2
    else:
        raise Exception("Новые уровни еще не добавлены!")


def calculate_habits(user: User, habits) -> int:
    count_habits = 0
    for habit in habits:
        if habit.user == user:
            count_habits += 1

    if (count_habits < 0):
        raise Exception("Количество привычек ниже нуля.")

    return count_habits


def get_user_awards(user: User, habits) -> []:
    user_habits = []
    for habit in habits:
        if habit.user == user and habit.is_done:
            user_habits.append(habit.award)

    return user_habits
