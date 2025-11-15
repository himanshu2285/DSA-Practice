'''
pattern 2
* 
* *
* * *
* * * *
* * * * *

'''


num = 6
for i in range(num):
    for j in range(i):
        print("*", end=" ")
    print()
    
    