class Garage:
    def __init__(self):
        self.parked_vehicle = None

    def setVehicle(self, vehicle):
        self.parked_vehicle = vehicle

    def __str__(self):
        if self.parked_vehicle:
            return f"Description of the parked vehicle:\n{self.parked_vehicle}"
        else:
            return "The garage is empty."

