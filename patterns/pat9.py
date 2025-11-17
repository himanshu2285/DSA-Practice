
'''
Pattern 7(Upper and lower Pyramid Star Pattern)
formula: space= n-i-1, star=2*i+1
        *
      * * *       
    * * * * *
  * * * * * * *
* * * * * * * * *
* * * * * * * * * 
  * * * * * * *   
    * * * * *     
      * * *       
        *
'''


class solution:
    def print_pattern(self, num):
        self.num = num
        # upper pyramid
        for i in range(num):  # 0 1 2 3 4
            # Space 
            for j in range(num - i - 1):
                print(" ", end=" ")
            # Stars
            for k in range(2 * i + 1):
                print("*", end=" ")
            # Space
            for j in range(num - i - 1):
                print(" ", end=" ")
            print()
        # lower pyramid
        for i in range(num-1, -1, -1):
            for j in range(num - i -1):
                print(" ", end=" ")
            for k in range(2 * i + 1):
                print("*", end=" ")
            for j in range(num - i -1):
                print(" ", end=" ")
            print()

obj = solution()
obj.print_pattern(6)