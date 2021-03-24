#Solving the Rush Hour Game
#Jessica McGRahan 
#S5164013

N = 6
EMPTY = '.'
#This function helps aim the visual display of the board
def visual_board(board):
    count = 1
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
    for letters in line:
        row.append(letters)
        if len(row) == 6:
            board.append(row)
            row = []
    return board

def board_format(board):
  return '\n'.join(''.join(_) for _ in board)

def get_sols(all_lines):
    sols = []
    past_line = False
    next_line = False
    for line in all_lines:
        #if past_line == True:
            #if not len(line.strip()) == 0 :
                #solution_elements = line.rstrip().split()      # strips line of "/n" and splits it into values by spaces
                #solution_elements.pop(0)                       # pops the "Sol:" string
                #sols.append(solution_elements)                 # adds to list
                #past_line = True
        if line.__contains__('Sol:'):
            solution_items = line.rstrip().split()      # strips line of "/n" and splits it into values by spaces
            solution_items.pop(0)                       # pops the "Sol:" string
            sols.append(solution_items)                 # adds to list
            past_line = True                 
        else:
            past_line = False
    return sols

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
