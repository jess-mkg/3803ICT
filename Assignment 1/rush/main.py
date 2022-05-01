from tools import structure_boards
from tools import Tools
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

if __name__ == "__main__":

    file = open('rh.txt', 'r')
    lines = file.readlines()
    boards = lines[4:44]
    b_sols = get_solutions(lines)
    s_boards = structure_boards(boards)
    #op, start, end = welcome()
    
    start = 0
    end = 15
    
    #if op == 'BFS':
    s = time.time()
    
    for i in range(start, end):
        t = Tools()
        #t.BFS(i, s_boards, b_sols)     #Breath First Search
        #t.ID(i, s_boards, b_sols, limit = 1)   #depth limited DFS
        #t.IDA1(i, s_boards, b_sols)    #blocking exit amount 
        #t.IDA2(i, s_boards, b_sols)    #cars blocking cars amount 
        #t.IDA3(i, s_boards, b_sols)    #sols length known
        #t.H1AStar(i, s_boards, b_sols)
        #t.H2AStar(i, s_boards, b_sols)
        #t.HillClimbGreedy(i, s_boards, b_sols)
        #t.HillClimbRandom(i, s_boards, b_sols)
        t.HCR(i, s_boards, b_sols)
        #t.SimAnn(i, s_boards, b_sols)

    e = time.time()
    print("Total Time: " + (str(e-s)))


#Heuristics
#Checks if the last move made increases the number of vehicles free to move
#Did the last move place a car in a position to which no other car can move