

def calculate(line):
    inp_amount = len(line)


def take_input(text, file=False):
    if file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                calculate(line)        
    else:
        calculate(text)


def main():
    file = open('input.txt', 'r')

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