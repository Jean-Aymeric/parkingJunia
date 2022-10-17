from abc import ABC, abstractmethod




class IParking(ABC):

    @abstractmethod
    def park(self, parking  ):
        ...

    @abstractmethod
    def unPark(self, parking ):
        ...

