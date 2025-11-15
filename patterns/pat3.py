'''
Pattern 3(column wise same number)
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''
num = 6
for i in range(num):
    for j in range(i):
        print(j+1, end=" ")
    print()