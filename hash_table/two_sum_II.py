from typing import List
class Solution:
    def twosum2(self, numbers: List[int], target):
        left=0
        right=len(numbers)-1
        for num in numbers:
            current_sum=numbers[left]+numbers[right]
            if current_sum==target:
                return [left+1, right+1]
            elif current_sum>target:
                right-=1
            else:
                left+=1


obj = Solution()
print(obj.twosum2([2,7,11,15], 9))
print(obj.twosum2([2,3,4], 6))
print(obj.twosum2([-1,0], -1))