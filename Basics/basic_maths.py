# 1. Count all digits in a number
class Solution_DigitsCount:
    def countDigits(self, num: int) -> int:
        sign = 1 if num >= 0 else -1
        num = abs(num)
        count = 0
        while num > 0:
            # rem = num % 10
            num //= 10
            count += 1
        return count
obj = Solution_DigitsCount()
print(obj.countDigits(110))


# 2. Reverse a number
class Solution_Reverse:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            rem = x % 10
            rev = rev * 10 + rem
            x //= 10
        
        return rev * sign
    
obj = Solution_Reverse()
print(obj.reverse(-1230))
    

# 3. Palindrome Number
class Solution_Palindrome:
    def isPalindrome(self, x: int) -> bool:
        orig = x
        sign = "-" if x < 0 else ""
        x = abs(x)
        rev = 0
        while(x>0):
            rem = x % 10
            rev = rev * 10 + rem
            x //= 10
        return orig == rev if sign == "" else False
obj = Solution_Palindrome()
print(obj.isPalindrome(10))
        

# 4. Armstrong Number
class Solution_Armstrong:
    def isArmstrong(self, n: int) -> bool:
        # sign = 1 if n>=0 else -1
        orig = n
        sign = '-' if n < 0 else ''
        n = abs(n)
        sum = 0
        while(n>0):
            rem = n % 10
            sum += rem ** 3
            n //= 10
        return sum == orig if sign == '' else False
obj = Solution_Armstrong()
print(obj.isArmstrong(0))



# 5. Print all the divisors of a number
# 1st approach
class Solution_Divisors:
    def printDivisors(self, n: int) -> list[int]:
        divisors = []
        for i in range(1, n+1):
            if n % i == 0:
                divisors.append(i)
        return divisors
obj = Solution_Divisors()
# print(obj.printDivisors(78))
# This code's time is O(n) because we are iterating from 1 to n to find the divisors.

# 2nd approach - Optimized
from math import sqrt
class Solution_Divisors2:
    def printDivisors(self, n: int) -> list[int]:
        divisors = []
        for i in range(1, int(sqrt(n))+1):
            if n % i == 0:
                divisors.append(i)
                if n // i != i:  # To avoid adding the square root twice for perfect squares
                    divisors.append(n // i)
        divisors.sort()  # Sort the divisors in ascending order
        return divisors
obj = Solution_Divisors2()
print(obj.printDivisors(36))
# Time Complexity = O(sqrt(N))