
import sys
import time

class NextCase:

    def __init__(self):
        self.l1 = []
        self.l2 = []
        self.l3 = ''

    def loadData(self, case):
        self.l1 = [int(x) for x in case[0]]     # makes list values ints
        self.l2 = [int(x) for x in case[1]]     # makes list values ints
        self.l3 = case[2]                       # heads or tails
    
    def sumDigits(self, number):        #finds the sum of digits 
        sum = 0
        while(number != 0):
            sum = sum + number % 10
            number = number // 10
        return sum

    def maxScore(self):
        kTurns = self.l1[1]     # turns each player can have per round
        starter = self.l3[0]    # who starts the game
        balls = []           
        sumD = []
        for i, ball in enumerate(self.l2):
            sumD.append([i, self.sumDigits(ball), ball])
            balls.append([i, ball])
        sumD.sort(reverse= True, key=lambda var: var[2])
        sumD.sort(reverse= True, key=lambda var: var[1])
        balls.sort(reverse= True, key=lambda var: var[1])
        rusty = []
        scott = []
        for j in range(self.l1[0]): #loops over the amount of balls present
            k = 0
            c = 0
            if starter == 'TAILS' and sumD:             # if its tails and sumD is not empty 
                while (k < kTurns) and sumD:            # 
                    k += 1
                    msd = sumD[0]
                    index = msd[0]
                    #delete from both lists
                    for i in balls:
                        if i[0] == index:
                            rusty.append(i[1])
                            balls.remove(i)
                            break    
                    sumD.remove(msd)
                if k == kTurns and balls:
                    starter = 'HEADS'     
            elif starter == 'HEADS' and balls:
                while (c < kTurns)and balls:    
                    c += 1
                    msd = balls[0]
                    scott.append(msd[1])
                    index = msd[0]
                    #delete from both lists
                    for i in sumD:
                        if i[0] == index:
                            sumD.remove(i)
                            break    
                    balls.remove(msd)
                if c == kTurns and sumD:
                    starter = 'TAILS'
            else:
                break
        print(sum(scott), sum(rusty))
      
if __name__ == "__main__":
    filename ='input.txt'
    #filename =input("Enter Filename: ")
    with open(filename) as f:
        lines = f.readlines()
        numCases = lines[0]
        cases = []                                      # list to hold all cases
        case = []                                       # list to hold each case
        for i in range(1, len(lines)):                  # loop over lines
            lines[i] = lines[i].rstrip().split()        # strip and split line
            case.append(lines[i])                       # add line to case
            if len(case) == 3:                          # if case has 3 elements 
                cases.append(case)                      # apeend
                case = []                               # reset case
    for i in cases:
        start = time.time()             # start timer
        c = NextCase()                  # create an object for the next case
        c.loadData(i)                   # load to wanted data
        c.maxScore()                    # find the scores
        print(time.time() - start)      # end timer 
        print('')