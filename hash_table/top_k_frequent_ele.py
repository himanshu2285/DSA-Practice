from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for ch in nums:
            freq[ch] = freq.get(ch,0)+1
        
        # sort by frequency
        sorted_nums = sorted(freq, key=freq.get, reverse=True)
    
        return sorted_nums[:k]

obj = Solution()
print(obj.topKFrequent([1,1,1,2,2,3], 2))