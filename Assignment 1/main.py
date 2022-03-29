
from pickle import FALSE
import pandas as pd
from collections import deque


LOCATIONS = deque()
for i in range(6):
        for j in range(6):
            l = [i,j]
            LOCATIONS.append(l)
print(LOCATIONS)


def get_solutions(lines):
    sols = []
    phrase = 'Sol:'
    end = '.' 
    lineNum = 0        
    for line in lines:                              #reads each line
        if phrase in line:                          #if 'Sol:' appears in a line the algo will preform some steps to append the solution to a list
            sol = line
            loopCount = 1
            while end not in sol:
                nex = lines[lineNum + loopCount]
                new = sol + nex
                sol = new
                loopCount +=1
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
    print(" 1 2 3 4 5 6")
    print("+-----------+")
    print(" ", end="")
    print(*board_format(board))
    print("+-----------+")

def check_right(board, pos, letter):
    if pos[1] != 5:
        if board[pos[0]][pos[1] + 1] == letter:
            return True

def check_left(board, pos, letter):
    if pos[1] != 0:
        if board[pos[0]][pos[1] - 1] == letter:
            return True

def check_down(board, pos, letter):
    if pos[0] != 5:
        if board[pos[0] + 1][pos[1]] == letter:
            return True

def check_up(board, pos, letter):
    if pos[0] != 0:
        if board[pos[0] - 1][pos[1]] == letter:
            return True


def find_vehicles(board):
    
    queue = LOCATIONS
    vehicle_dict = {"Location":[],"Size":[],"Axis":[],"Letter":[]}
    

    while queue: 

        pos = queue.popleft()
        
        if board[pos[0]][pos[1]] != '.':
            new_vehicle = []
            letter = board[pos[0]][pos[1]]
            size = 0

            if pos[1] != 5:
                size2 = check_right(board, pos, letter)
                if size2:
                    size = 2
                    index = []
                    pos[1] += 1
                    queue.remove(pos)
                    size3 = check_right(board, pos, letter)
                    if size3:
                        size = 3
                        pos[1] += 1
                        queue.remove(pos)
                    print(letter + ": vehicle found with size " + str(size))
                    #vehicle_dict["Location"].append(index)
                    
            if pos[0] != 5:
                size2 = check_down(board, pos, letter)
                if size2:
                    size = 2
                    pos[0] += 1
                    queue.remove(pos)
                    size3 = check_down(board, pos, letter)
                    if size3:
                        pos[0] += 1
                        queue.remove(pos)
                        size = 3
                    print(letter + ": vehicle found with size " + str(size))




goal_pos = [2,4],[2,5]
EMPTY_SPACE = '.'
solved = False


file = open('rh.txt', 'r')
lines = file.readlines()
boards = lines[4:44]
b_sols = get_solutions(lines)
s_boards = structure_boards(boards)

for i in range(0,1):
    print('[' , i+1 , ']') 
    
    start_board = s_boards[i]
    vehicle_dict = dict()
    explored = deque()
    queue = deque()
    queue.append(start_board)
    
    visual_board(queue[0])
    print('Proposed Solution:' , end=' ')
    print(*b_sols[i], sep = ", ")
    print('\n')
    
    if queue:
        current = queue.popleft();
        if current[2][4] == 'X' and current[2][5] == 'X':
            solved = True
            print('Solved!')
        else:
            vehicle_dict = find_vehicles(current)

    else:
        print("FAILED")

    print('\n')




