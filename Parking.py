from IParking import IParking



class Parking :

    __vehicles : [IParking]

    def __init__(self):
        self.__vehicles = []

    def addVehicle(self, vehicle : IParking):
        if vehicle not in self.__vehicles:
            self.__vehicles.append(vehicle)
            vehicle.park(self)

    def getVehicles(self)-> [str] :
        temp = []
        for vehicle in self.__vehicles :
            temp.append(vehicle.getName())
        return temp

    def removeVehicle(self, vehicle : IParking):
        self.__vehicles.remove(vehicle)