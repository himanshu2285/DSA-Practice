from typing import List
class Solution:
    def contains_duplicate2(self, nums: List[int], k: int) -> bool:
        seen={}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            
            seen[num]=i
        return False
    
obj =  Solution()
print(obj.contains_duplicate2(nums = [1,2,3,1], k=3))
print(obj.contains_duplicate2(nums = [1,0,1,1], k = 1))
print(obj.contains_duplicate2(nums = [1,2,3,1,2,3], k = 2))