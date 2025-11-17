'''
Pattern 10: Half Diamond Star Pattern
* 
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''

class solution:
    def print_pattern(self, num):
        for i in range(num):
            for j in range(i):
                print("*", end=" ")
            print()
        for i in range(num-2, 0, -1):
            for j in range(i):
                print("*", end=" ")
            print()

obj = solution()
obj.print_pattern(6)