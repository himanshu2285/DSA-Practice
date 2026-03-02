# 1. Print Name N times using Recursion
class Solution:
    def printName(self, name: str, n: int) -> None:
        if n <= 0:
            return
        print(name)
        self.printName(name, n-1)
obj = Solution()
obj.printName("Alice", 5)


