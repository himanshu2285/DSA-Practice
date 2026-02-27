# 1st approach (Not work well for negative numbers, because python keeps remainder positive for negative numbers)

# class Solution:
#     def reverse(self, x: int) -> int:
#         rev = 0
#         while(x!=0):
#             rem = x % 10
#             rev = rev * 10 + rem
#             x = x // 10
#         return rev
    
# obj = Solution()
# print(obj.reverse(-1230))


# 2nd Approuch
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            rem = x % 10
            rev = rev * 10 + rem
            x //= 10
        
        return rev * sign
    
obj = Solution()
print(obj.reverse(-1230))
    
