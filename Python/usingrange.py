start = int(input("Enter the Starting Range: "))
end = int(input("Enter the End Range: "))
print("prime numbers in the range",start,"to",end)
for i in range( start, end+1 ):
    flag = 0
    for j in range(2 , i):
        if (i % j == 0):
            flag = 1
            break

    if (flag == 0):
        print( i , end = ' ')
