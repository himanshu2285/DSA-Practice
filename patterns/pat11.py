'''
Pattern - 11: Binary Number Triangle Pattern
0 
1 0
0 1 0
1 0 1 0
0 1 0 1 0

'''


class solution:
    def print_pattern(self, num):
        for i in range(num):
            if i % 2 == 0:
                start = 1
            else:
                start = 0
            for j in range(i):
                print(start, end=" ")
                # Flip between 0 and 1
                start = 1 - start
            print()
            
obj = solution()
obj.print_pattern(6)