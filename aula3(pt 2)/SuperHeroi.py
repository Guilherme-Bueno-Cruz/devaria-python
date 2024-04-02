import abc

class SuperHeroi(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def poder(self):
        pass
