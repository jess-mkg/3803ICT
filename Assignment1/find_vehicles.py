
def boundaries(self, board, yrows, xcols, direction):
    v_id = board[yrows,xcols]
    v = Vehicle()
    v.handle = v_id
    
    is_car = Cars().find_cars(board, yrows, xcols, direction, v, handle)
    if is_car:
        return is_car

    is_truck = Trucks().find_trucks(board, yrows, xcols, direction, v, handle)
    if is_truck:
        return is_truck
    

def borders(n):
    return (n < 6 and n >= 0)

class Vehicle:
    handle = -1
    size = -1
    moved = False
    location = []
    direction = None
    
class Cars():
    def find_cars(self, board, yrows, xcols, direction, vehicle, handle):
        if direction == 'h':
            next_h = 1
            next_v = 0
            vehicle.direction = 'h'
        elif direction == 'v':
            next_h = 0
            next_v = 1
            vehicle.direction = 'v'
        if borders(yrows+next_h) and borders(xcols+next_v):
            if board[yrows+next_v,xcols+next_h] == board[yrows,xcols] == handle:
                position = [{'x':xcols, 'y':yrows},{'x':xcols+next_h, 'y':yrows+next_v}]
                vehicle.location = position
                vehicle.size = 2
                return vehicle
        return None
class Trucks():
    def find_trucks(self, board, yrows, xcols, direction, vehicle, handle):
        if direction == 'h':
            next_h = 2
            next_v = 0
            vehicle.direction = 'h'
        elif direction == 'v':
            next_h = 0
            next_v = 2
            vehicle.direction = 'v'
        if borders(yrows+next_v) and borders(yrows-next_v) and borders(xcols+next_h) and borders(xcols-next_h):
            if board[yrows+next_v,xcols+next_h] == board[yrows-next_v,xcols-next_h] == handle:



