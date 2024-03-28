import abc


class Repository(abc.ABC):
    @abc.abstractmethod
    def add_user(self):
        pass

    @abc.abstractmethod
    def get_user(self):
        pass

    @abc.abstractmethod
    def get_users(self):
        pass

    @abc.abstractmethod
    def add_award(self):
        pass

    @abc.abstractmethod
    def get_award(self):
        pass

    @abc.abstractmethod
    def get_awards(self):
        pass

    @abc.abstractmethod
    def add_habit(self):
        pass

    @abc.abstractmethod
    def get_habit(self):
        pass

    @abc.abstractmethod
    def get_habits(self):
        pass
