from abc import abstractmethod, ABC


class Vehicle(ABC) :

    __name : str

    def __init__(self, name : str):
        self.__name = name

    def getName(self) -> str :
        return self.__name

    @abstractmethod
    def drive(self):
        ...