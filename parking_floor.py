
class ParkingFloor:
    def __init__(self, parking_lot_id, floor_no, total_slots):
        self.parking_lot_id = parking_lot_id
        self.floor_no = floor_no
        self.total_slots = total_slots
        self.parking_slots = []
        # vehicle_type: occupied slot_number
        self.vehicle_occupied_slots_map = {}
        self.vehicle_free_slots_map = {}
        self.initialize_slots()

    def __str__(self):
        return f"{self.parking_lot_id}_{self.floor_no}"

    
    def initialize_slots(self):
        for slot_no in range(1, self.total_slots+1):
            slot = ParkingSlot(self.parking_lot_id, floor_no=self.floor_no, slot_no=slot_no)
            self.parking_slots.append(slot)
            self.add_or_append_vehicle_slots_map(self.vehicle_free_slots_map, slot.slot_type, slot.slot_no)
            self.vehicle_occupied_slots_map[slot.slot_type] = set()
    
    def has_available_parking_slot(self, vehicle_type):
        for slot in self.parking_slots:
            if slot.slot_type == vehicle_type and slot.is_available:
                return slot
        return False

    def add_or_append_vehicle_slots_map(self, map, vehicle_type, slot_no):
        map[vehicle_type] = map.get(vehicle_type, set())
        map[vehicle_type].add(slot_no)
        return map

    def park_on_available_slot(self, slot, vehicle):
        if slot.is_available is True:
            slot.vehicle = vehicle
            vehicle_type = slot.slot_type
            self.remove_from_vehicle_occupied_slots_map(self.vehicle_free_slots_map, slot.vehicle_type, slot.slot_no)
            self.add_or_append_vehicle_slots_map(self.vehicle_occupied_slots_map ,slot.slot_type, slot.slot_no)
            slot.is_available = False
        else:
            raise Exception(f"Slot {slot} already occupied")

    def remove_from_vehicle_occupied_slots_map(self, map, vehicle_type, slot_no):
        used_slots = map[vehicle_type]
        if slot_no in used_slots:
            used_slots.remove(slot_no)

    def unpark_on_slot(self, slot):
        if slot.is_available is True:
            print("Slot is already available")
            return 
        else:
            print(f"Unparked vehicle with Registration Number: {slot.vehicle.reg_no} and Color: {slot.vehicle.color}")
            slot.vehicle = None
            slot.is_available = True
            self.remove_from_vehicle_occupied_slots_map(self.vehicle_occupied_slots_map ,slot.vehicle_type, slot.slot_no)
            self.add_or_append_vehicle_slots_map(self.vehicle_free_slots_map ,slot.slot_type, slot.slot_no)

    def display(self, display_type, vehicle_type):
        if display_type == "free_count":
            return self.display_free_count(vehicle_type)
        if display_type == "free_slots":
            return self.display_free_slots(vehicle_type)
        return self.display_occupied_slot(vehicle_type)

    def display_set(self, _set):
        return ",".join([str(i) for i in list(_set)])

    def display_free_slots(self, vehicle_type):
        _set = self.vehicle_free_slots_map[vehicle_type]
        print(f"Free slots for {vehicle_type} on Floor {self.floor_no}:", self.display_set(_set))
    
    def display_occupied_slot(self, vehicle_type):
        occupied_slots = self.vehicle_occupied_slots_map[vehicle_type]
        print(f"Occupied slots for {vehicle_type} on Floor {self.floor_no}:", self.display_set(occupied_slots))
    
    def display_free_count(self, vehicle_type):
        occupied_slots = self.vehicle_occupied_slots_map[vehicle_type]
        free_slots = self.vehicle_free_slots_map[vehicle_type]
        print(f"Free slots for {vehicle_type} on Floor {self.floor_no}:", abs(len(free_slots - occupied_slots)))





class ParkingSlot:
    def __init__(self, parking_lot_id, floor_no, slot_no, slot_type=None, vehicle=None):
        self.parking_lot_id = parking_lot_id
        self.floor_no = floor_no
        self.slot_no = slot_no
        self.is_available = True
        if slot_type is None:
            self.slot_type = self.get_slot_type()
        else:
            self.slot_type = slot_type
        
        self.vehicle_type = self.slot_type
        self.vehicle = vehicle

    def get_slot_type(self):
        from vehicle import VehicleType
        if self.slot_no == 1:
            return VehicleType.TRUCK
        elif self.slot_no <= 3:
            return VehicleType.BIKE
        else:
            return VehicleType.CAR

    def __str__(self):
        return f"{self.parking_lot_id}_{self.floor_no}_{self.slot_type}_{self.slot_no}"
