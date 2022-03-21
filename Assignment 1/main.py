
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




file = open('rh.txt', 'r')
lines = file.readlines()
boards = lines[4:44]
b_sols = get_solutions(lines)
s_boards = structure_boards(boards)

for i in range(0,1):
    print(i+1)
    visual_board(s_boards[i])
    print(s_boards[i])
    #print('Proposed Solution: ')
    #print(*b_sols[i], sep = ", ")
    print('\n')


