class Ticket:
    def __init__(self, parking_lot_id, floor_no, slot_no, vehicle):
        self.ticket_id = f"{parking_lot_id}_{floor_no}_{slot_no}"
        self.parking_lot_id = parking_lot_id
        self.floor_no = floor_no
        self.slot_no = slot_no
        self.vehicle = vehicle
    
    def __str__(self):
        return f"{self.ticket_id}"