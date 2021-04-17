
KEY = {
    '.': 0,
    'A': 2,
    'B': 2,
    'C': 2,
    'D': 2,
    'E': 2,
    'F': 2,
    'G': 2,
    'H': 2,
    'I': 2,
    'J': 2,
    'K': 2,
    'O': 3,
    'P': 3,
    'Q': 3,
    'R': 3,
    'X': 1,
}

MOVEMENT = {
    LEFT: "left", 
    RIGHT: "right",
    UP: "up"
    DOWN: "down",
}

def goal_state_achived(vehicle):
    if vehicle.position[0]['X'] == 4 and vehicle.position[1]['X'] == 5:
        if vehicle.handle == 1:
            return True
    return False


def boundaries(board, yrows, xcols, direction):
    v_id = board[yrows][xcols]
    v = Vehicle()
    v.handle = v_id
    if v_id != 0:
        is_car = Cars().find_cars(board, yrows, xcols, direction, v, v.handle)
        if is_car:
            return is_car
        is_truck = Trucks().find_trucks(board, yrows, xcols, direction, v, v.handle)
        if is_truck:
            return is_truck
     

def borders(n):
    return (n < 6 and n >= 0)

class Vehicle:
    def __init__(self):
        self.handle = -1
        self.size = -1
        self.moved = False
        self.location = []
        self.direction = None

    
class Cars(Vehicle):
    def __init__(self):
        super().__init__()
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
            if board[yrows-next_v][xcols-next_h] == handle:
                position = [{'x':xcols, 'y':yrows},{'x':xcols+next_h, 'y':yrows+next_v}]
                vehicle.location = position
                vehicle.size = 2
                return vehicle
        
class Trucks(Vehicle):
    def __init__(self):
        super().__init__()
    def find_trucks(self, board, yrows, xcols, direction, vehicle, handle):
        if direction == 'h':
            next_h = 2
            next_v = 0
            vehicle.direction = 'h'
        elif direction == 'v':
            next_h = 0
            next_v = 2
            vehicle.direction = 'v'
        #if borders(yrows+next_v) and borders(yrows-next_v) and borders(xcols+next_h) and borders(xcols-next_h):
        if borders(yrows+next_v) and borders(yrows-next_v) and borders(xcols+next_h) and borders(xcols-next_h):
            #if board[yrows+next_v][xcols+next_h] == board[yrows-next_v][xcols-next_h] == handle:
            if board[yrows+next_v][xcols+next_h] == handle:
                if board[yrows-next_v][xcols-next_h] == handle:
                    #position = [{'x':xcols-next_h, 'y':yrows-next_v}, {'x':xcols, 'y':yrows}, {'x':xcols+next_h, 'y':yrows+next_v}]
                    position = [{'x':xcols-next_h, 'y':yrows-next_v}, {'x':xcols, 'y':yrows}, {'x':xcols+next_h, 'y':yrows+next_v}]
                    vehicle.location = position
                    vehicle.size = 3
                    return vehicle
