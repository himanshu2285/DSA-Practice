'''
Pattern 6(row wise same number in reverse order)
5 5 5 5 5 
4 4 4 4 
3 3 3
2 2
1
'''



num = 6
for i in range(num-1, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()