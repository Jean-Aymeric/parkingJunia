from Vehicle import Vehicle


class Tank(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self,name)

    def drive(self):
        print("Je Drive comme un Tank")
