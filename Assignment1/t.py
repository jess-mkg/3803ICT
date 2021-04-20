

st = "ABCDEFGHIJK"
tr = "OPRQ"
red = "X"

b = 'G'
 
for letter in b:
    if letter in st:
        print(True)
    elif letter in tr:
        print("Wrong")
    elif letter in red:
        print("wrong again")

