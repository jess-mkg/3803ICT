
number = 1              # allows the while to be maintained at the start
count = 0               # initialise count
while number != 0:      # only when the number is 0 will it stop
    number = int(input("Enter a number: "))     # user input
    if number > 0:                              # if the number is positive it will be counted
        count += 1                              # add to count

print(count, end=" ")                           # print the count on the same line at the statement
print("positive numbers were entered.")         # concluding statement 

