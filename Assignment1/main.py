import find_vehicles
from tools_rh import Tools


#main
#Open the text file and read lines 8 - 48 which are the 40 problems
if __name__ == "__main__":
    goal_state_bfs = Tools()
    file = open("Assignment1/rh.txt", "r")
    lines = file.readlines()
    solutions = goal_state_bfs.get_sols(lines)
    lines = lines[8:48]
    num_sol = 0

    board = []
    for line in lines: 
        goal_state_bfs = Tools()
        board = goal_state_bfs.get_board(board, line)
        goal_state_bfs.bfs(board)
        print("\nProposed Solution: ", end=" ")
        print(solutions[num_sol])
        print("\n")
        num_sol += 1

    file.close()

