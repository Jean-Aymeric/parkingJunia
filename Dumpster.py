from IParking import IParking
from Parking import Parking



class Car(IParking) :

    __name : str

    def park(self, parking: Parking):
        parking.addVehicle(self)

    def unPark(self, parking : Parking):
        parking.removeVehicle(self)

    def __init__(self, name):
        self.__name = name

    def getName(self)-> str:
        return self.__name


