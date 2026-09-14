from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}
        for i in range(0, n):
            rem = target - nums[i]
            if rem in hashmap:
                return [hashmap[rem], i]
            hashmap[nums[i]]=i

obj = Solution()
print(obj.twoSum([2,7,11,15], 13))
print(obj.twoSum([3,2,4], 6))
print(obj.twoSum([3,3], 6))
print(obj.twoSum([3], 3))