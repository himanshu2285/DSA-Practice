
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Selection Sort Algorithm
        for i in range(n-1):
            mini = i
            for j in range(i+1, n):
                if nums[j] < nums[mini]:
                    mini = j
            # Swap after finding the minimum element
            nums[i], nums[mini] = nums[mini], nums[i]
        return nums
    
obj = Solution()
print(obj.sortArray([64, 25, 12, 22, 11]))


# Time Complexity: O(n^2) due to the nested loops.
# Space Complexity: O(1) as it is an in-place sorting algorithm.