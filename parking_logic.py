import math

def calculate_distance(car_x, car_y, slot_x, slot_y):
    return round(math.sqrt((slot_x - car_x) ** 2 + (slot_y - car_y) ** 2), 2)

def get_direction(car_x, slot_x):
    if car_x < slot_x - 20:
        return "TURN RIGHT"
    elif car_x > slot_x + 20:
        return "TURN LEFT"
    return "STRAIGHT"

def parking_status(distance):
    if distance < 50:
        return "PARKED"
    elif distance < 150:
        return "SLOW DOWN"
    return "SEARCHING"