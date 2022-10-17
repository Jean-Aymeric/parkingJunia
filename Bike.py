from IParking import IParking
from Parking import Parking
from Vehicle import Vehicle


class Bike(Vehicle, IParking) :
    def park(self, parking: Parking):
        parking.addVehicle(self)

    def unPark(self, parking : Parking):
        parking.removeVehicle(self)

    def __init__(self, name):
        Vehicle.__init__(self,name)

    def drive(self):
        print("Je Drive comme un vélo")
