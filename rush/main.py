from tools import structure_boards
from tools import Tools
from tools import visual_board
from tools import welcome
import time



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

def print_res(res):
    if res[2] == "SOLVED":
        print("Algorithm: " + res[0])
        print("Card Number: " + str(res[1]))
        print("Status: " + res[2])
        visual_board(res[3])
        print(res[4])
        visual_board(res[5])
        print(res[6])
        print("Depth: " + str(res[7]))
        print("Nodes: " + str(res[8]))
        print("Different in Sol Lenth: " + str(res[9]))
        print("Time: " + str(res[10]))
        print("Accuracy: " + str(res[11]))
        print("\n")
    
    elif res[2] == "FAILED":
        print("Algorithm: " + res[0])
        print("Card Number: " + str(res[1]))
        print("Status: " + res[2])
        visual_board(res[3])
        print(res[4])
        
        print("Depth: " + str(res[7]))
        print("Nodes: " + str(res[8]))
        print("Time: " + str(res[10]))
        print("\n")


if __name__ == "__main__":

    file = open('rh.txt', 'r')
    lines = file.readlines()
    boards = lines[4:44]
    b_sols = get_solutions(lines)
    s_boards = structure_boards(boards)
    #op, start, end = welcome()

    start = 0
    end = 40

    total = 0
    diff = 0 
    fail_count = 0
    get_depths = []

    s = time.time()
    for i in range(start, end):
        
        t = Tools()
        #if op == "BFS":
        #print_res(res)
        #res = t.BFS(i, s_boards, b_sols)     #Breath First Search
        #if op == "ID":
        res = t.ID(i, s_boards, b_sols, limit = 1)   #depth limited DFS
        #print_res(res)
        #if op == "AStar1":
        #res = t.H1AStar(i, s_boards, b_sols)
        #print_res(res)
        #if op == "AStar2":
        #res = t.H2AStar(i, s_boards, b_sols)
        #print_res(res)
        #if op == "HC": 
        #res = t.HCStart(i, s_boards, b_sols)
        #print_res(res)
        #if op == "SA":
        #res = t.SAStart(i, s_boards, b_sols)
        print_res(res)
        total +=res[11]
        diff += res[9]
        get_depths.append(res[7])
        if res[2] == "FAILED":
            fail_count += 1
    e = time.time()
    print("Total Fail Count: " + str(fail_count))
    print("Total Difference: " + str(diff))
    print("Total Accuracy: " + str(total/(end-start)))
    print("Total Time: " + (str(e-s)))
    print(get_depths)

