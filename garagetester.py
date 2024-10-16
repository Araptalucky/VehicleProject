from truck import Truck  # Import Truck class
from garage import Garage  # Import Garage class

class GarageTester:
    @staticmethod
    def getExample():
        truck = Truck(color="black", has_trailer=False)
        garage = Garage()
        garage.setVehicle(truck)
        return garage

