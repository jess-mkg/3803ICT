from inspect import stack
from logging import NullHandler
from collections import deque
import time


def welcome():

    print(" _____           _       _    _                     _____                      ")
    print("|  __ \         | |     | |  | |                   / ____|                     ")
    print("| |__) |   _ ___| |__   | |__| | ___  _   _ _ __  | |  __  __ _ _ __ ___   ___ ")
    print("|  _  / | | / __| '_  \ |  __  |/ _ \| | | | '__| | | |_ |/ _` | '_ ` _ \ / _ \ ")
    print(
        "| | \ \ |_| \__ \ | | | | |  | | (_) | |_| | |    | |__| | (_| | | | | | |  __/")
    print("|_|  \_\__,_|___/_| |_| |_|  |_|\___/ \__,_|_|     \_____|\__,_|_| |_| |_|\___| ")
    print("\n")
    print("Welcome!")

    options = ['BFS', 'ID']

    while True:
        try:
            print("Choose formula by typing it in: ")
            print("Options:", end=" ")
            for i in options:
                print(i, end=" ")
            op = input("\n$ ")
            if op not in options:
                print("Sorry, I didn't understand that ... ")
                continue
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break

    while True:
        try:
            print("Enter range of problems to analyse: ")
            start = int(input("Enter first value in range:\n$ "))
            end = int(input("Enter second value in range:\n$ "))

            if start < 0 or start > 40 or end < 0 or end > 40 or start == 39 or end == 0:
                print("Sorry, not valid ... ")
                continue

            if start > end:
                print("Sorry, value 1 cant be larger than value 2 ... ")
                continue

            if not isinstance(start, int) or not isinstance(end, int):
                print("Sorry, value 1 and/or 2 is not a number ... ")
                continue

        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return op, start, end

def get_solutions(lines):
    sols = []
    phrase = 'Sol:'
    end = '.'
    lineNum = 0
    for line in lines:  # reads each line
        if phrase in line:  # if 'Sol:' appears in a line the algo will preform some steps to append the solution to a list
            sol = line
            loopCount = 1
            while end not in sol:
                nex = lines[lineNum + loopCount]
                new = sol + nex
                sol = new
                loopCount += 1
            arrsol = sol.split()
            del arrsol[0]
            del arrsol[(len(arrsol)-1)]
            sols.append(arrsol)
        lineNum += 1
    return sols

def structure_boards(boards):
    arrs = []
    arr = []
    for board in boards:
        row = []
        for letter in board:
            row.append(letter)
            if len(row) == 6:
                arr.append(row)
                row = []
        arrs.append(arr)
        arr = []
    return arrs

def board_format(board):
    return '\n'.join(''.join(_) for _ in board)

def visual_board(board):
    print(" 0 1 2 3 4 5")
    print("+-----------+")
    print(" ", end="")
    print(*board_format(board))
    print("+-----------+")

class Tools:

    def __init__(self):
        self.child_nodes = deque()

    def check_right(self, board, pos):
        if pos[1] < 5:
            return board[pos[0]][pos[1] + 1]

    def check_left(self, board, pos):
        if pos[1] > 0:
            return board[pos[0]][pos[1] - 1]

    def check_down(self, board, pos):
        if pos[0] < 5:
            return board[pos[0] + 1][pos[1]]

    def check_up(self, board, pos):
        if pos[0] > 0:
            return board[pos[0] - 1][pos[1]]

    def find_vehicles(self, board):

        queue = deque([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [
                      2, 5], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]])
        vehicle_dict = {"Location": [], "Size": [], "Axis": [], "Letter": []}

        while queue:
            pos = queue.popleft()  # pop left from the queue (FIFO)
            if board[pos[0]][pos[1]] != '.':  # only look and letters
                letter = board[pos[0]][pos[1]]
                size = 0
                direction = ''

                if pos[1] != 5:
                    size2 = self.check_right(board, pos)
                    if size2 == letter:  # Checks for a size 2 vehicles
                        size = 2
                        pos[1] += 1
                        queue.remove(pos)  # removes pos from queue to search
                        direction = 'h'
                        # stores the location of found vehicle
                        index = [[pos[0], pos[1]-1], [pos[0], pos[1]]]
                        # check if its a truck with the size of 3
                        size3 = self.check_right(board, pos)

                        if size3 == letter:  # Checks for a size 3 vehicle s
                            size = 3
                            pos[1] += 1
                            queue.remove(pos)  # removes from queue
                            index = [[pos[0], pos[1]-2],
                                     [pos[0], pos[1]-1], [pos[0], pos[1]]]
                        # append locations, size, axis, and letter of the vehicle to a dictionary
                        vehicle_dict["Location"].append(index)
                        vehicle_dict["Size"].append(size)
                        vehicle_dict["Axis"].append(direction)
                        vehicle_dict["Letter"].append(letter)

                if pos[0] != 5:
                    size2 = self.check_down(board, pos)
                    if size2 == letter:
                        size = 2
                        pos[0] += 1
                        queue.remove(pos)
                        direction = 'v'
                        index = [[pos[0]-1, pos[1]], [pos[0], pos[1]]]
                        size3 = self.check_down(board, pos)

                        if size3 == letter:
                            size = 3
                            pos[0] += 1
                            queue.remove(pos)
                            index = [[pos[0]-2, pos[1]],
                                     [pos[0]-1, pos[1]], [pos[0], pos[1]]]
                        vehicle_dict["Location"].append(index)
                        vehicle_dict["Size"].append(size)
                        vehicle_dict["Axis"].append(direction)
                        vehicle_dict["Letter"].append(letter)

        return vehicle_dict

    def next_depth_board(self, board, letter, location, axis, size):

        c_location = [[location[x][y] for y in range(
            len(location[0]))] for x in range(len(location))]

        if axis == "up":
            old = c_location[-1]
            board[old[0]][old[1]] = "."
            new = c_location[0]
            board[new[0]-1][new[1]] = letter

            for i in range(size):
                c_location[i][0] -= 1
            return board, c_location

        elif axis == "down":
            old = c_location[0]
            board[old[0]][old[1]] = "."
            new = c_location[-1]
            board[new[0]+1][new[1]] = letter

            for i in range(size):
                c_location[i][0] += 1
            return board, c_location

        elif axis == "left":
            old = c_location[-1]
            board[old[0]][old[1]] = "."
            new = c_location[0]
            board[new[0]][new[1]-1] = letter

            for i in range(size):
                c_location[i][1] -= 1
            return board, c_location

        elif axis == "right":
            old = c_location[0]
            board[old[0]][old[1]] = "."
            new = c_location[-1]
            board[new[0]][new[1]+1] = letter

            for i in range(size):
                c_location[i][1] += 1
            return board, c_location

    def possible_moves_left(self, board, location, size, letter, direction, rec_depth, chain):
        if direction == NullHandler or direction == "left":
            og_board = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]
            c_location = location[:]
            pos = [c_location[0][0], c_location[0][1]]
            left = self.check_left(og_board, pos)
            if left == ".":
                rec_depth += 1
                next, c_location = self.next_depth_board(og_board, letter, location, "left", size)
                action = self.form_action(letter, "L", rec_depth)
                new = chain[:]
                new.append(action)
                self.child_nodes.append((next, new))
                self.possible_moves_left(next, c_location, size, letter, "left", rec_depth, chain)

    def possible_moves_right(self, board, location, size, letter, direction, rec_depth, chain):
        if direction == NullHandler or direction == "right":
            og_board = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]
            c_location = location[:]
            pos = [c_location[-1][0], c_location[-1][-1]]
            right = self.check_right(og_board, pos)
            if right == ".":
                rec_depth += 1
                next, c_location = self.next_depth_board(og_board, letter, location, "right", size)
                action = self.form_action(letter, "R", rec_depth)
                new = chain[:]
                new.append(action)
                self.child_nodes.append((next, new))
                self.possible_moves_right(next, c_location, size, letter, "right", rec_depth, chain)

    def possible_moves_down(self, board, location, size, letter, direction, rec_depth, chain):
        if direction == NullHandler or direction == "down":
            og_board = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]
            c_location = location[:]
            pos = [c_location[-1][0], c_location[-1][1]]
            down = self.check_down(og_board, pos)
            if down == '.':
                rec_depth += 1
                next, c_location = self.next_depth_board(og_board, letter, location, "down", size)
                action = self.form_action(letter, "D", rec_depth)
                new = chain[:]
                new.append(action)
                self.child_nodes.append((next, new))
                self.possible_moves_down(next, c_location, size, letter, "down", rec_depth, chain)

    def possible_moves_up(self, board, location, size, letter, direction, rec_depth, chain):
        if direction == NullHandler or direction == "up":
            og_board = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]
            c_location = location[:]
            pos = [c_location[0][0], c_location[0][1]]
            down = self.check_up(og_board, pos)
            if down == '.':
                rec_depth += 1
                next, c_location = self.next_depth_board(og_board, letter, location, "up", size)
                action = self.form_action(letter, "U", rec_depth)
                new = chain[:]
                new.append(action)
                self.child_nodes.append((next, new))
                self.possible_moves_up(next, c_location, size, letter, "up", rec_depth, chain)

    def form_action(self, letter, direction, amount):
        a1 = letter + direction
        a2 = str(amount)
        a3 = a1+a2
        return a3


    def BFS(self, i, board, sols):
        print('[', i, ']')
        start_board = board[i]
        chain = []
        start = (start_board, chain)       
        explored = set()
        queue = deque()
        vehicle_dict = dict()
        
        queue.append(start)
        explored.add(str(start_board))
        print('Proposed Solution:', end=' ')
        print(*sols[i], sep=", ")

        depth = 0
        nodes = 0

        s = time.time()

        while queue:
            depth += 1
            current = queue.popleft()
            explored.add(str(current[0]))
            
            if current[0][2][4] == 'X' and current[0][2][5] == 'X':
                print('Solved!')
                visual_board(current[0])
                
                print("Found Solution: ", end="")
                for i in current[1]:
                    if i == current[1][-1]:
                        print(i, end=" ")
                    else:
                        print (i, end=", ")
                print("\n")
                break
            else:
                vehicle_dict = self.find_vehicles(current[0])
                num_of_veh = len(vehicle_dict['Location'])
                rec_depth = 0

                for i in range(0, num_of_veh):
                    loc = vehicle_dict['Location'][i]
                    size = vehicle_dict['Size'][i]
                    axis = vehicle_dict['Axis'][i]
                    letter = vehicle_dict['Letter'][i]
                    if axis == 'h':
                        self.possible_moves_left(
                            current[0], loc, size, letter, NullHandler, rec_depth, current[1])
                        self.possible_moves_right(
                            current[0], loc, size, letter, NullHandler, rec_depth, current[1])
                    elif axis == 'v':
                        self.possible_moves_down(
                            current[0], loc, size, letter, NullHandler, rec_depth, current[1])
                        self.possible_moves_up(
                            current[0], loc, size, letter, NullHandler, rec_depth, current[1])

                    for node in self.child_nodes:
                        nodes += 1
                        if str(node[0]) not in explored:
                            queue.append(node)
                            explored.add(str(node[0]))
                    self.child_nodes.clear()
        else:
            print("FAILED")

        queue.clear()
        e = time.time()
        print("Time: " + (str(e-s)) + "\nDepth:" +
            str(depth) + "\nNodes:" + str(nodes) + "\n")

    
    def ID(self, i, board, sols):
        print('[', i, ']')
        start_board = board[i]
        chain = []
        start = (start_board, chain)       
        explored = set()
        queue = deque()
        vehicle_dict = dict()
        
        queue.append(start)
        visual_board(start_board)
        explored.add(str(start_board))
        
        depth = 0
        nodes = 0
        depth_limit = 1

        s = time.time()

        while queue:
            depth += 1
            current = queue.popleft()
            
            add = current[0]
            explored.add(str(current[0]))
            
            if current[0][2][4] == 'X' and current[0][2][5] == 'X':
                print('Solved!')
                visual_board(current[0])
                print("Found Solution: " + str(current[1]))
                print("Depth found at: " + str(depth_limit))
                print("\n")
                break
            else:
                vehicle_dict = self.find_vehicles(current[0])
                num_of_veh = len(vehicle_dict['Location'])
                rec_depth = 0

                for d in range(1,depth_limit+1):
                    for i in range(0, num_of_veh):
                        loc = vehicle_dict['Location'][i]
                        size = vehicle_dict['Size'][i]
                        axis = vehicle_dict['Axis'][i]
                        letter = vehicle_dict['Letter'][i]
                        if axis == 'h':
                            self.possible_moves_left(
                                current[0], loc, size, letter, NullHandler, rec_depth, current[1])
                            self.possible_moves_right(
                                current[0], loc, size, letter, NullHandler, rec_depth, current[1])
                        elif axis == 'v':
                            self.possible_moves_down(
                                current[0], loc, size, letter, NullHandler, rec_depth, current[1])
                            self.possible_moves_up(
                                current[0], loc, size, letter, NullHandler, rec_depth, current[1])

                        for node in self.child_nodes:
                            if str(node[0]) not in explored:
                                queue.appendleft(node)
                                nodes += 1
                        self.child_nodes.clear()
        else:
            print("FAILED")

        queue.clear()
        e = time.time()
        print("Time: " + (str(e-s)) + "\nDepth:" +
            str(depth) + "\nNodes:" + str(nodes) + "\n")