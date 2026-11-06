class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i, val in enumerate(nums):
            if target==val:
                return i
        return -1