"""
Parking Lot
    floor 1
        - slot 1
            - slot_type
        - slot 2
        - slot 3

        - slot n
    floor 2
        - slot 1
        - slot 2
        - slot n

Vehicle
    - vehicle_no
    - type
    - color
    - owner_name

Ticket
    - ticken_no
    - vehicle
    - vehicle_entered_at
    - vehicle_exited_at
    - parking_lot
    - floor_no
    - slot_no

"""
from parking_floor import ParkingFloor
from ticket import Ticket
from vehicle import Vehicle

class ParkingLot:
    def __init__(self, parking_lot_id, total_floors, slot_per_floor):
        self.parking_lot_id = parking_lot_id
        self.total_floors = total_floors
        self.slots_per_floor = slot_per_floor
        self.floors = []
        self.tickets = {}
        self.initialize_floors()
    
    def initialize_floors(self):
        for idx in range(1, self.total_floors+1):
            floor = ParkingFloor(self.parking_lot_id, floor_no=idx, total_slots=self.slots_per_floor)
            self.floors.append(floor)
        print(f"Created parking lot with {len(self.floors)} floors and {self.floors[0].total_slots} slots per floor")
        
    
    def park_vehicle(self, vehicle_type, reg_no, color):
        for floor in self.floors:
            available_slot = floor.has_available_parking_slot(vehicle_type)
            if available_slot:
                vehicle = self.create_vehicle(vehicle_type, reg_no, color)
                floor.park_on_available_slot(available_slot, vehicle)
                ticket = self.create_ticket(floor.floor_no, slot_no=available_slot.slot_no, vehicle=vehicle)
                self.tickets[ticket.ticket_id] = ticket
                print(f"Parked vehicle. Ticket ID: {ticket.ticket_id}")
                # print(self.tickets)
                return ticket
        return None

    def create_vehicle(self, vehicle_type, reg_no, color):
        return Vehicle(vehicle_type, reg_no, color)

    def create_ticket(self, floor_no, slot_no, vehicle):
        return Ticket(parking_lot_id=self.parking_lot_id, floor_no=floor_no, slot_no=slot_no, vehicle=vehicle)

    
    def get_floor_from_ticket_id(self, ticket_id):
        floor_no = int(ticket_id.split("_")[1])
        return self.floors[floor_no-1]

    def get_slot_from_ticket_id(self, ticket_id):
        floor = self.get_floor_from_ticket_id(ticket_id=ticket_id)
        slot_no = int(ticket_id.split("_")[2])
        return floor.parking_slots[slot_no-1]

    def unpark_vehicle(self, ticket_id):
        # print(f"existing tickets: {self.tickets}")
        if ticket_id not in self.tickets:
            print("Invalid Ticket")
            return
        floor = self.get_floor_from_ticket_id(ticket_id)
        # print("unpark floor", floor)
        slot = self.get_slot_from_ticket_id(ticket_id)
        # print("unpark slot", slot)
        floor.unpark_on_slot(slot)
        # exit(1)
        self.tickets.pop(ticket_id)

        return True

    def display(self, display_type, vehicle_type):
        for floor in self.floors:
            floor.display(display_type, vehicle_type)