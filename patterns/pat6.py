'''
Pattern 6(column wise same number in reverse order)
1 2 3 4 5 
1 2 3 4 
1 2 3
1 2
1
'''



num = 6
for i in range(num-1, 0, -1):
    for j in range(i):
        print(j+1, end=" ")
    print()