''' Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''



from typing import List

nums = [2,7,11,15] 
target = 13

class Solution:
    def two_Sum(self, nums: List[int], target: int) -> List[int]:
        val_idx = {}
        for i, num in enumerate(nums):
            if target-num in val_idx:
                return [val_idx[target-num], i]
            val_idx[num] = i
            
obj = Solution()
print(obj.two_Sum(nums, target))