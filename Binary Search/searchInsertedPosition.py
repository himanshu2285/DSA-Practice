class Solution:
    def searchInsertPosition(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left


### this approuch only pass 58/68 test case
'''class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if target in nums:
            for i in range(len(nums)):
                if target==nums[i]:
                    return i
        else:
            if target > max(nums):
                return len(nums)
            elif target < min(nums):
                return 0
            else:
                mid = (left + right) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                return mid'''
