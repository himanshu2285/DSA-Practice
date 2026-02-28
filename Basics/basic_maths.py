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
        
