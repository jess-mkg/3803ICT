

number = int(input("Enter a positive number: "))
count = 0           #initialise count for the 4 values wanted per line
f1, f2 = 0, 1       #initialise 0 and 1 

for element in range(number):   # Loop over the value given by the user input
    if element == 0:            # The values 0 and 1 are delt with differently
        print(f1, end=' ')      # as it can cause issues with negative values
    elif element == 1:          # to add n-1 and n-2 if n = 0, same for n = 1
        print(f2, end=' ')
    else:
        newf = f1 + f2          # add the n-1 and n-2 values for the next value
        f1 = f2                 # set the values for the next calculation
        f2 = newf
        print(newf, end=' ')    # end=' ' lets all values be on the same line
    count += 1                  # adds to count
    if count == 4:              # when the count is 4 we want a new line
        print("\t")             # used tab instead of newline as newline was adding a blank line between the 4 output numbers
        count = 0               # reset the count value for the next 4 values


