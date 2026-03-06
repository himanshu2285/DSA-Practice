# 1. Print Name N times using Recursion
class Solution:
    def printName(self, name: str, n: int) -> None:
        if n <= 0:
            return
        print(name)
        self.printName(name, n-1)
obj = Solution()
obj.printName("Alice", 2)


# 2. Print 1 to N using Recursion
class Solution_Print:
    def printOneToN(self, n: int) -> None:
        if n <= 0:
            return
        self.printOneToN(n-1)
        print(n)
obj = Solution_Print()
obj.printOneToN(5)
print()

# 3. Print N to 1 using Recursion
class Solution_Print:
    def printNum(self, n: int) -> None:
        if n <= 0:
            return
        print(n)
        self.printNum(n-1)
obj = Solution_Print()
obj.printNum(5)
print()

# 4. Sum of first N natural numbers using Recursion
class Solution_Sum:
    def fun(self, num:int, sum:int) -> int:
        if num <= 0:
            return sum
        return self.fun(num-1, sum+num)
obj = Solution_Sum()
print(obj.fun(100, 0))
print()

# 5. Factorial of a number using Recursion
class Solution_Factorial:
    def factorial(self, n: int) -> int:
        if n < 0:
            return -1  # Factorial is not defined for negative numbers
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n-1)
obj = Solution_Factorial()
print(obj.factorial(5))
print()

# 2nd method
class Solution_fact:
    def fun(self, n:int, fact:int) -> None:
        if n<0:
            print("Enter Positive Number")
            return # To stop function
        else:
            if n==0:
                return fact
            return self.fun(n-1, fact*n)
obj = Solution_fact()
print(obj.fun(5, 1))


# 6. Check if a string is palindrome or not 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left = 0 
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))


# 7. Fibonacci Series using Recursion
class Solution_Fib:
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
obj = Solution_Fib()
print(obj.fib(10))
print()
# Fibonacci Series without Recursion

class Fibonacci:
    def find_fibb(self, num:int)->int:
        a,b=0,1
        print(a)
        for _ in range(num):
            sum=a+b 
            print(sum)
            a=b 
            b=sum
obj = Fibonacci()
obj.find_fibb(2)
print()

# OR Leetcode Solution
class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
obj = Solution()
print(obj.fib(4))
print()



# 8. Reverse a list without recursion
class ReverseList:
    def reverse(self, lst):
        left, right = 0, len(lst) - 1
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        return lst
obj = ReverseList()
print(obj.reverse([1, 2, 3, 4, 5]))