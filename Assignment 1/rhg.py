import cProfile
from copy import deepcopy
from logging import NullHandler
from collections import deque
import time

solved = False

def welcome():
 print(" _____           _       _    _                     _____                      ")
 print("|  __ \         | |     | |  | |                   / ____|                     ")
 print("| |__) |   _ ___| |__   | |__| | ___  _   _ _ __  | |  __  __ _ _ __ ___   ___ ")
 print("|  _  / | | / __| '_  \ |  __  |/ _ \| | | | '__| | | |_ |/ _` | '_ ` _ \ / _ \ ")
 print("| | \ \ |_| \__ \ | | | | |  | | (_) | |_| | |    | |__| | (_| | | | | | |  __/")
 print("|_|  \_\__,_|___/_| |_| |_|  |_|\___/ \__,_|_|     \_____|\__,_|_| |_| |_|\___| ")
 print("\n")
 print("Welcome!")
                                                                                
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
    print(" 0 1 2 3 4 5")
    print("+-----------+")
    print(" ", end="")
    print(*board_format(board))
    print("+-----------+")

def check_right(board, pos):
    if pos[1] < 5:
        return board[pos[0]][pos[1] + 1]

def check_left(board, pos):
    if pos[1] > 0:
        return board[pos[0]][pos[1] - 1] 

def check_down(board, pos):
    if pos[0] < 5:
        return board[pos[0] + 1][pos[1]]

def check_up(board, pos):
    if pos[0] > 0:
        return board[pos[0] - 1][pos[1]] 

def find_vehicles(board):
    
    queue = deque([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]])
    vehicle_dict = {"Location":[],"Size":[],"Axis":[],"Letter":[]}
    
    while queue: 
        pos = queue.popleft()                                           #pop left from the queue (FIFO)
        if board[pos[0]][pos[1]] != '.':                                #only look and letters
            letter = board[pos[0]][pos[1]]
            size = 0
            direction= ''

            if pos[1] != 5:
                size2 = check_right(board, pos)
                if size2 == letter:                                               #Checks for a size 2 vehicles
                    size = 2
                    pos[1] += 1
                    queue.remove(pos)                                   #removes pos from queue to search
                    direction = 'h'
                    index = [[pos[0], pos[1]-1], [pos[0], pos[1]]]      #stores the location of found vehicle
                    size3 = check_right(board, pos)             #check if its a truck with the size of 3
                    
                    if size3 == letter:                                           #Checks for a size 3 vehicle s
                        size = 3
                        pos[1] += 1
                        queue.remove(pos)                               #removes from queue
                        index = [[pos[0], pos[1]-2], [pos[0], pos[1]-1], [pos[0], pos[1]]]
                    vehicle_dict["Location"].append(index)              #append locations, size, axis, and letter of the vehicle to a dictionary
                    vehicle_dict["Size"].append(size)
                    vehicle_dict["Axis"].append(direction)
                    vehicle_dict["Letter"].append(letter)

            if pos[0] != 5:
                size2 = check_down(board, pos)   
                if size2 == letter:                                               
                    size = 2
                    pos[0] += 1
                    queue.remove(pos)                                  
                    direction = 'v'
                    index = [[pos[0]-1, pos[1]], [pos[0], pos[1]]]      
                    size3 = check_down(board, pos)              
                    
                    if size3 == letter:
                        size = 3
                        pos[0] += 1
                        queue.remove(pos)
                        index = [[pos[0]-2, pos[1]], [pos[0]-1, pos[1]], [pos[0], pos[1]]]
                    vehicle_dict["Location"].append(index)
                    vehicle_dict["Size"].append(size)
                    vehicle_dict["Axis"].append(direction)
                    vehicle_dict["Letter"].append(letter)
    
    return vehicle_dict

def next_depth_board(board, letter, location, axis, size):
    
    c_location = [[location[x][y] for y in range(len(location[0]))] for x in range(len(location))]

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
            c_location[i][1] -=1 
        return board, c_location

    elif axis == "right":
        old = c_location[0]
        board[old[0]][old[1]] = "."
        new = c_location[-1]
        board[new[0]][new[1]+1] = letter
        
        for i in range(size):
            c_location[i][1] += 1
        return board, c_location

new_move = {"board":[],"action":[]}           #global var to hold, probably not a good idea

def possible_moves_left(board, location, size, letter, direction, rec_depth): 
    if direction == NullHandler or direction == "left":
        
        og_board = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]
        c_location = location[:]
        
        pos = [c_location[0][0], c_location[0][1]]
        left = check_left(og_board, pos)
        if left == ".":
            rec_depth += 1
            next, c_location = next_depth_board(og_board, letter, location, "left", size)
            if next not in explored:
                queue.append(next)
                explored.append(next)
                #visual_board(next)
                new_move["board"].append(next)
                #action = form_action(letter, "L", rec_depth)
                #new_move["action"].append(action)
            possible_moves_left(next, c_location, size, letter, "left", rec_depth)         
            
def possible_moves_right(board, location, size, letter, direction, rec_depth): 
    if direction == NullHandler or direction == "right":
        
        og_board = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]
        c_location = location[:]    
        
        pos = [c_location [-1][0], c_location[-1][-1]]
        right = check_right(og_board, pos)
        if right == ".":
            rec_depth += 1
            next, c_location = next_depth_board(og_board, letter, location, "right", size)
            if next not in explored:
                queue.append(next)
                explored.append(next)
                #visual_board(next)
                new_move["board"].append(next)
                #action = form_action(letter, "R", rec_depth)
                #new_move["action"].append(action)
            possible_moves_right(next, c_location, size, letter, "right", rec_depth)

def possible_moves_down(board, location, size, letter, direction, rec_depth):
    if direction == NullHandler or direction == "down":
        
        og_board = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]
        c_location = location[:]
        
        pos = [c_location[-1][0], c_location[-1][1]]
        down = check_down(og_board, pos)
        if down == '.':
            rec_depth += 1
            next, c_location = next_depth_board(og_board, letter, location, "down", size)
            if next not in explored:
                queue.append(next)
                explored.append(next)
                #visual_board(next)
                new_move["board"].append(next)
                #action = form_action(letter, "D", rec_depth)
                #new_move["action"].append(action)
            possible_moves_down(next, c_location, size, letter, "down", rec_depth)

def possible_moves_up(board, location, size, letter, direction, rec_depth):
    if direction == NullHandler or direction == "up":
        
        og_board = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]
        c_location = location[:]
        
        pos = [c_location[0][0], c_location[0][1]]
        down = check_up(og_board, pos)
        if down == '.':
            rec_depth += 1
            next, c_location = next_depth_board(og_board, letter, location, "up", size)
            if next not in explored:
                queue.append(next)
                explored.append(next)
                #visual_board(next)
                new_move["board"].append(next)
                #action = form_action(letter, "U", rec_depth)
                #new_move["action"].append(action)
            possible_moves_up(next, c_location, size, letter, "up", rec_depth)
    
def form_action(letter, direction, amount):
    a1 = letter + direction
    a2 = str(amount)
    a3 = a1+a2
    return a3

explored = deque()
queue = deque()

def bfs(start, end, boards, sols):
    for i in range(start, end):
        
        print('[' , i , ']') 
        start_board = boards[i]
        chain = (start_board, [])
        print(chain)
        vehicle_dict = dict()
        queue.append(start_board)
        visual_board(start_board)
        
        print('Proposed Solution:' , end=' ')
        print(*sols[i], sep = ", ")
        print('\n')  
        depth = 0
        nodes = 0
        s = time.time()
        while queue:
            depth += 1
            current = queue.pop();
            explored.append(current)            #add curr board to explored state so it isnt seen twice
            if current[2][4] == 'X' and current[2][5] == 'X':
                print('Solved!')
                visual_board(current)       #print the board in the goal state
                break                       #If solution is found
            else:
                vehicle_dict = find_vehicles(current)               #Find the vehicles on the current board  
                num_of_veh = len(vehicle_dict['Location']) 
                      
                for i in range(0,num_of_veh):
                    loc = vehicle_dict['Location'][i]
                    size = vehicle_dict['Size'][i]
                    axis = vehicle_dict['Axis'][i]
                    letter = vehicle_dict['Letter'][i]
                    rec_depth = 0
                    
                    if axis == 'h':
                        possible_moves_left(current, loc, size, letter, NullHandler, rec_depth)
                        possible_moves_right(current, loc, size, letter, NullHandler, rec_depth)
                    elif axis == 'v':
                        possible_moves_down(current, loc, size, letter, NullHandler, rec_depth)  
                        possible_moves_up(current, loc, size, letter, NullHandler, rec_depth) 
                    
                n = len(new_move["board"])
                nodes += n
            

        else:       
            print("FAILED")
        print('\n')
        new_move["board"].clear()
        new_move["action"].clear()
        queue.clear
        explored.clear
        e = time.time()
        print("time: ", end="")
        print(e-s)
        print("Depth", end=" ")
        print(depth)
        print("Nodes", end=" ")
        print(nodes)
    
def main():

    file = open('rh.txt', 'r')
    lines = file.readlines()
    boards = lines[4:44]
    b_sols = get_solutions(lines)
    s_boards = structure_boards(boards)

    options = ['BFS']

    welcome()

    #while True:
     #   try:
      #      print("Choose formula by typing it in: ")
       #     print("Options:", end=" ")
        #    for i in options:
         #       print(i, end=" ")
          #  op = input("\n$ ")

        #    if op not in options:
         #       print("Sorry, I didn't understand that ... ")
          #      continue

    #    except ValueError:
     #       print("Sorry, I didn't understand that.")
      #       #try again, return to the start of loop
       #     continue
    
    #    else:
     #       break

    #while True:
    #    try:
     #       print("Enter range of problems to analyse: ")
     #       start = int(input("Enter first value in range:\n$ "))
     #       end = int(input("Enter second value in range:\n$ "))

    #        if start < 0 or start > 40 or end < 0 or end > 40 or start == 39 or end == 0:
     #           print("Sorry, not valid ... ")
      #          continue

      #      if start > end:
       #         print("Sorry, value 1 cant be larger than value 2 ... ")
        #        continue
            
      #      if not isinstance(start, int) or not isinstance(end, int):
       #         print("Sorry, value 1 and/or 2 is not a number ... ")
        #        continue

    #    except ValueError:
     #       print("Sorry, I didn't understand that.")
      #      continue
    
    #    else:
     #       break
    
    
    start = 0
    end = 1
    
    #if op == 'BFS':
    bfs(start, end, s_boards, b_sols)


if __name__ == "__main__":
    main()

#cProfile.run('main()')