from vehicle import Vehicle  # Import Vehicle class

class Car(Vehicle):
    def __init__(self, color, has_winter_tires=False):
        super().__init__(color)
        self.has_winter_tires = has_winter_tires

    def __str__(self):
        vehicle_description = super().__str__()
        return f"{vehicle_description}\nHas winter tires: {self.has_winter_tires}"
