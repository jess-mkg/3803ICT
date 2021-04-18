

def calculate(line):
    line = line.split()
    inp_amount = len(line)
    if inp_amount == 0:
        return 0
    elif inp_amount == 1:
        print("1")
    elif inp_amount == 2:
           print("2") 
    elif inp_amount == 3:
        print("3")

    return inp_amount #return the amount of values in a line

def take_input(lines, file=True):
    if file:
        while True:
            file_lines = lines.readlines()
            if not file_lines:
                break
            else:
                for line in file_lines:
                    count = calculate(line)
                    print(count)  
    else:
        count = calculate(lines)
        print(count) 


def main():
    file = open('2801/input.txt', 'r')
    #text = 5
    take_input(file)


if __name__ == "__main__":
    main()


#sample output
#6
#7
#9
#2
#10
#57
#14839
#278083
#4307252
#32100326
#410623254
#1589266556