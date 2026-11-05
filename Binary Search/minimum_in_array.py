# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def minInSortedArray(self, nums: list[int]) -> int:
        result = sorted(nums)
        return result[0]
obj = Solution()
print(obj.minInSortedArray([4,5,6,7,0,1,2]))