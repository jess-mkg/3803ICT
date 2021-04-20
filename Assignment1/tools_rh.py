#Solving the Rush Hour Game
#Jessica McGRahan 
#S5164013
import find_vehicles
import collections
from collections import deque
import numpy
import copy
 
N = 6
EMPTY = '.'

def board_format(board):
        return '\n'.join(''.join(_) for _ in board)

class Tools:

    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.queue = deque()
        self.seen_boards = {}
        self.previous_board = {}
        self.count = 0
        self.seen = []

    #This function helps aim the visual display of the board
    def visual_board(self, board):
        print(" 1 2 3 4 5 6")
        print("+-----------+")
        print(" ", end="")
        print(*board_format(board))
        print("+-----------+")
        print(" a b c d e f")

    #data structure that holds each problem cards board set up 
    def get_board(self, board, line):
        board = []
        line = line[:-1]
        row = []
        for letter in line:
            row.append(letter)
            if len(row) == 6:
                board.append(row)
                row = []
        self.visual_board(board)
        print(board)
        board = self.fix_board(line, board)
        return board

    def fix_board(self, line, board):
        matrix = line.split("\n")
        index = list()
        numy = 0
        for r in board:
            numx = 0
            for location in r:
                index.append({'char': find_vehicles.KEY[location], 'y': numy, 'x':numx})
                numx = numx + 1
            numy = numy + 1
        final_board = numpy.zeros(shape=(6, 6))
        for position in index:
            final_board[position['y'], position['x']] = position['char']
        print(final_board)
        return final_board


    def get_sols(self, all_lines):
        sols = []
        for line in all_lines:
            if line.__contains__('Sol:'):
                solution_items = line.rstrip().split()      # strips line of "/n" and splits it into values by spaces  
                solution_items.pop(0)                       # pops the "Sol:" string
                sols.append(solution_items)                 # adds to list
        return sols

    def bfs(self, board):
        nodes = 0
        goat_state = None
        solved = False
        self.previous_boards(board, None)
        print("BFS: ")
        carsntrucks = self.vehicles(board)
        while self.queue:
            print("h")
            other_board = self.queue.popleft()
            carsntrucks = vehicles(other_board)
            if (goal_state_achived(goat_state)):
                if goal_state != None and not solved:
                    print("CPU Time: : ")
                    print("Depth: ")
                    print("Difference: ")
                    print("Nodes Searched: " + str(count))
                    solved = True
                    break
            goal_state = self.search(other_board, carsntrucks)
            node += 1
            print(node)
        return self.seen_boards


    def vehicles(self, board):
        automobiles = []
        for yrow, i in enumerate(board):
            for xcols, j in enumerate(i):
                vehicle = self.find_on_board(board, yrow, xcols)
                double = False
                #print(vehicle.size)
                for vehicle_ID in automobiles:
                    if vehicle is None:
                        break
                    if vehicle_ID == vehicle:
                        double = True
                        break
                if not vehicle or double:
                    continue
                automobiles.append(vehicle)
        return automobiles     

#get the direction value 
    def find_on_board(self, board, y, x):
        board_value = board[y][x]
        if board_value != 0:
            h = find_vehicles.boundaries(board, y, x, 'h')
            v = find_vehicles.boundaries(board, y, x, 'v')
            if h:
                return h
            if v:
                return v

    def search(self, board, automobiles):
        goal_state = False
        for car_truck in automobiles:
            if car_truck.handle == 1:
                goal_state = True
            if (car_truck.direction == 'h'):
                move_L = {'left': empty_spots(board, car_truck, 'left')}
                move_R = {'right': empty_spots(board, car_truck, 'right')}
                self.move_automobile(board, car_truck, move_L)
                self.move_automobile(board, car_truck, move_R)
            else:   # going in a direction and knowing how mant empty spots are in front of it 
                move_U = {'up': empty_spots(board, car_truck, 'up')}
                move_D = {'down': empty_spots(board, car_truck, 'down')}
                self.move_automobile(board, car_truck, move_U)
                self.move_automobile(board, car_truck, move_D)
            vehicle.reset_moved()
        return goal_state

    def empty_spots(board, vehicle, movement):
        empty_spots = 1
        is_valid = True
        x_axis = vehicle.location[0]['x']
        y_axis = vehicle.location[0]['y']
        i_size = vehicle.size - 1
        #horezontal
        if movement == 'left':
            next_h = -1
            next_v = 0
        elif movement == 'right':
            next_h = 1
            next_v = 0
        #vertical
        elif movement == 'up':
            next_h = 0
            next_v = -1
        elif movement == 'down':
            next_h = 0
            next_v = 1
        
        while is_valid:
            y = next_v * empty_spots + y 
            x = next_h * empty_spots + x
            if borders(y) and board(x) and board[y][x] == 0:
               empty_spots += 1
            else:
                is_valid = False
        if empty_spots == 1:
            return 0
        else:
            return empty_spots-1
    
    def move_automobile(self, board, vehicle, direction):
        if not vehicle.moved:
            #Making a copy of the board 
            curr = copy.copy(board)
            #Making a deep copy for the x,y location attached to the object vehicle
            prev_vehicle = copy.deepcopy(vehicle.location)
            #The (string) direction of the vehicle
            string_direction = list(direction.keys())[0]
            #Gets the amount of moves to make
            amount_to_move = direction[string_direction] 
            #Makes the move value negative if left or up
            if string_direction == 'left' or string_direction == 'up':
                amount_to_move = -amount_to_move
            if string_direction == 'left' or string_direction == 'right':
                axis = 'x'
            if string_direction == 'up' or string_direction == 'down':
                axis = 'y'
            self.slider(board, vehicle, string_direction, axis, amount_to_move)
            self.update_board(board, vehicle, prev_vehicle)
        unseen = self.solution(board, curr)


    def previous_boards(self, board, prev_board):
        if not hash(board.tostring()) in self.previous_board:
            if prev_board is not None:
                prev_board = hash(prev_board.tostring())
            self.previous_board[hash(board.tostring())] = prev_board
            self.seen[hash(board.tostring())] = copy.copy(board)
            self.queue.append(copy.copy(board))
            return True
        return False

    
    def update_board(self, board, vehicle, prev_pos):
        if(vehicle.has_moved):
            for i, _ in enumerate(prev_pos):
                board[prev_pos[i]['y'], prev_pos[i]['x']] = 0
            for j, _ in enumerate(vehicle.location):
                board[vehicle.location[j]['y'], vehicle.location[j]['x']] = vehicle.handle

    
    def slider(self, board, vehicle, direction, axis, stepsize):
        approved = self.is_allowed(board, vehicle, direction, axis, stepsize)
        if approved:
            self.count += 1
            vehicle.moving_vehicle(axis, stepsize)
            return True
        return False

    def is_allowed(self, board, vehicle, direction, axis, stepsize):
        is_allowed = False
        if direction == 'left' or direction == 'up':
            is_allowed = find_vehicles.borders(vehicle.location[0][axis] + stepsize)
        elif direction == 'right' or direction == 'down':
            index = vehicle.size - 1
            is_allowed = find_vehicles.borders(vehicle.location[index][axis] + stepsize)
            
        if vehicle.direction == 'h' and axis == 'y':
            is_allowed = False

        if vehicle.direction == 'v' and axis == 'x':
            is_allowed = False

        # this is a guard that was necessary to correct for multiple movements of the same vehicle?
        # TURNS out we still want one vehicle movement per exploration of the board.
        if stepsize == 0 or vehicle.has_moved:
           is_allowed = False

        # check allowed or we are already out of bounds
        if is_allowed and not helper.is_board_position_empty_in_direction(board, vehicle, direction):
            is_allowed = False

        return is_allowed




