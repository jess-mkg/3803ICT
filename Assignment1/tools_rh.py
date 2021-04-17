#Solving the Rush Hour Game
#Jessica McGRahan 
#S5164013
import find_vehicles
import collections
from collections import deque
import numpy

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
        print("BFS: ")
        carsntrucks = self.vehicles(board)
        while self.queue:
            #if queue: 
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
            print("h")
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
            if car_truck.Vehicle().self.handle == 1:
                goal_state = True
            if (vehicle.direction == 'h'):
                move_L = 
                move_R = 
                
            else:
                move_U = 
                move_D = 

