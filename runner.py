from parking_lot import ParkingLot

cmds = """
create_parking_lot <parking_lot_id> <no_of_floors> <no_of_slots_per_floor>
park_vehicle <vehicle_type> <reg_no> <color>
unpark_vehicle <ticket_id>
display <display_type> <vehicle_type>
Possible values of display_type: free_count, free_slots, occupied_slots
exit
"""
print(cmds)
parking_lot_obj = None

while True:
    input_str = input()
    cmd, rest_arr = input_str.split(" ")[0], input_str.split(" ")[1:]
    if cmd == "create_parking_lot" and parking_lot_obj is None:
        parking_lot_id, total_floors, slots_per_floor = rest_arr
        parking_lot_obj = ParkingLot(parking_lot_id, int(total_floors), int(slots_per_floor))
    elif cmd == "park_vehicle":
        vehicle_type, reg_no, color = rest_arr
        ret = parking_lot_obj.park_vehicle(vehicle_type, reg_no, color)
        if ret is None:
            print("Parking Lot Full")
    elif cmd == "unpark_vehicle":
        ticket_id = rest_arr[0]
        # print(f"ticket_id {ticket_id} for unparking")
        parking_lot_obj.unpark_vehicle(ticket_id)
    elif cmd == "display":
        dispaly_type, vehicle_type = rest_arr
        parking_lot_obj.display(dispaly_type, vehicle_type)
    elif cmd == "exit":
        break



