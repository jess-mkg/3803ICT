#Solving the Rush Hour Game
#Jessica McGRahan 
#S5164013
import find_vehicles

N = 6
EMPTY = '.'
#This function helps aim the visual display of the board
def visual_board(board):
    print(" 1 2 3 4 5 6")
    print("+-----------+")
    print(" ", end="")
    print(*board_format(board))
    print("+-----------+")
    print(" a b c d e f")

#data structure that holds each problem cards board set up 
def get_board(line):
    board = []
    line = line[:-1]
    row = []
    for letter in line:
        row.append(letter)
        if len(row) == 6:
            board.append(row)
            row = []
    return board

def board_format(board):
  return '\n'.join(''.join(_) for _ in board)

def get_sols(all_lines):
    sols = []
    for line in all_lines:
        if line.__contains__('Sol:'):
            solution_items = line.rstrip().split()      # strips line of "/n" and splits it into values by spaces  
            solution_items.pop(0)                       # pops the "Sol:" string
            sols.append(solution_items)                 # adds to list
    return sols

def bfs(board):
    bfsq = []
    bfsq.append(board)  #start state
    seen = set()
    while bfsq:
        state = bfsq.pop(0)

def vehicles(board):
    vehicles = []
    for yrow in enumerate(board):
        for xcols in enumerate(yrow):
            vehicle = find_on_board(board, yrow, xcols)
            for vehicle_ID in vehicles:
                if vehicle is None or vehicle == vehicle_ID:
                    break
                if not vehicle:
                    continue
                vehicles.append(vehicle)
    return vehicles     


def find_on_board(board, y, x):
    if board[y,x] != EMPTY:
        h = find_vehicles.boundaries(board, y, x, 'h')
        v = find_vehicles.boundaries(board, y, x, 'v')
    if h:
        return h
    if v:
        return v




#main
#Open the text file and read lines 8 - 48 which are the 40 problems
if __name__ == "__main__":
    file = open("Assignment1/rh.txt", "r")
    lines = file.readlines()
    solutions = get_sols(lines)
    lines = lines[8:48]
    num_sol = 0

    board = []
    for line in lines:
        board = get_board(line)
        visual_board(board)
        print("\nProposed Solution: ", end=" ")
        print(solutions[num_sol])
        print("\n")
        num_sol += 1

    file.close()

