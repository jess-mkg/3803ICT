from tools import structure_boards
from tools import Tools
from tools import visual_board
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
        
        if res[0] != 'Greedy Hill Climbing' or res[0] != 'Simulated Annealing':
            i = 0
        else:
            visual_board(res[5])
            print(res[6])
        
        print("Depth: " + str(res[7]))
        print("Nodes: " + str(res[8]))
        print("Different in Sol Lenth: " + str(res[9]))
        print("Time: " + str(res[10]))
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

    start = 29
    end = 30
    
    #if op == 'BFS':
    s = time.time()
    
    for i in range(start, end):
        t = Tools()
        #res = t.BFS(i, s_boards, b_sols)     #Breath First Search
        #print_res(res)

        #res = t.ID(i, s_boards, b_sols, limit = 1)   #depth limited DFS
        #print_res(res)
        #res = t.IDA1(i, s_boards, b_sols)    #blocking exit amount 
        #print_res(res)
        #res = t.IDA2(i, s_boards, b_sols)    #cars blocking cars amount 
        #print_res(res)
        #res = t.IDA3(i, s_boards, b_sols)    #sols length known
        #print_res(res)
        #res = t.H1AStar(i, s_boards, b_sols)
        #print_res(res)
        #res = t.H2AStar(i, s_boards, b_sols)
        #print_res(res)
        #res = t.HCStart(i, s_boards, b_sols)
        #print_res(res)
        res = t.SimAnn(i, s_boards, b_sols)
        print_res(res)
    e = time.time()
    print("Total Time: " + (str(e-s)))


#Heuristics
#Checks if the last move made increases the number of vehicles free to move
#Did the last move place a car in a position to which no other car can move