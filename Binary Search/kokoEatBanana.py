class Solution:
    def koko_eating_banana(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            hour = 0
            for pile in piles:
                hour += (pile + mid - 1) // mid
            
            if hour > h:
                left = mid + 1
            else:
                right = mid
        
        return left

obj = Solution()
print(obj.koko_eating_banana([3,6,7,11], 8))
print(obj.koko_eating_banana([30,11,23,4,20], 5))
print(obj.koko_eating_banana([30,11,23,4,20], 6))