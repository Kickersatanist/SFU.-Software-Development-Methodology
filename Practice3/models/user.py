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

    def __eq__(self, other):
        if isinstance(other, User):
            return (
                    self.id == other.id and
                    self.name == other.name and
                    self.level == other.level and
                    self.awards == other.awards and
                    self.countHabits == other.countHabits
            )
        return False
