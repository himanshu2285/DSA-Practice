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