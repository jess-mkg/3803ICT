
number = int(input("Enter a positive number: ")) # user input

rows = 2 * (number) - 1                        # initialise the row size

for i in range(number):                        # loop over the users value for the top half
    print(" " *(number - i), "X" *(2 * i + 1)) # print x's on the top half of the diamond (including the middle line)
for i in range(number - 2, -1, -1):            # loops over the bottom, size starting at 2 less then the input value, going down to -1, at a rate of -1
    print(" " *(number - i), "X" *(2 * i + 1)) # print x's on the bottom half (starting below the middle line) of the diamond

# in line 7 and 9 there is " " * (number - i)
# this line creates the empty space needed to 
# display the diamond correctly
