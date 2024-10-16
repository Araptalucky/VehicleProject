from vehicle import Vehicle  # Import Vehicle class

class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)
        self.has_trailer = has_trailer

    def __str__(self):
        vehicle_description = super().__str__()
        return f"{vehicle_description}\nHas trailer: {self.has_trailer}"

