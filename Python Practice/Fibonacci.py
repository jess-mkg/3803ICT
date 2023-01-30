
number = int(input("Enter a positive number: "))
#print((number-1)+(number-2))
arr = []
for element in range(number):
    if element == 0:
        arr.append(0)
    elif element == 1:
        arr.append(1)
    else:
        arr.append(arr[element-1] + arr[element-2])

for i in range(0, number, 4):
    print(*arr[i:i+4], sep=' ')

