
'''
Pattern 7(Pyramid Star Pattern)
formula: space= n-i-1, star=2*i+1
        *
      * * *       
    * * * * *
  * * * * * * *
* * * * * * * * *
'''


num = 5
for i in range(num-1, -1, -1):  # 4 3 2 1 0
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