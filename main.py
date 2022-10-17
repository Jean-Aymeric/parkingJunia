from Bike import Bike
from Car import Car
from MotorBike import MotorBike
from Parking import Parking
from Tank import Tank

v1 = Car("Twingo")
v2 = Bike("BMX")
v3 = MotorBike("Tmax")
v4 = Tank("Char LeClerc")
p1 = Parking()
p1.addVehicle(v1)
p1.addVehicle(v2)
p1.addVehicle(v3)
#p1.addVehicle(v4)
print(p1.getVehicles())