class Solution:
    def binarySearch(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left<=right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return -1

obj = Solution()
print(obj.binarySearch([-1,0,3,5,9,12], 3))
print(obj.binarySearch([-1,0,3,5,9,12], 2))
print(obj.binarySearch([2], 2))