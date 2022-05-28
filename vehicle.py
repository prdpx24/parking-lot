class Vehicle:
    def __init__(self, vehicle_type, reg_no, color):
        self.vehicle_type = vehicle_type
        self.reg_no = reg_no
        self.color = color


class VehicleType:
    TRUCK = "TRUCK"
    CAR = "CAR"
    BIKE = "BIKE"