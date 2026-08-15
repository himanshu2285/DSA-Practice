strs = ["eat","tea","tan","ate","nat","bat"]
# output = [["bat"], ["nat", "tan"], ["ate","eat","tea"]]

from typing import List
class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}     # Hashmap to store sorted key and thier respective words
        for word in strs:
            key = ''.join(sorted(word))
            
            if key not in groups:
                groups[key]=[]
                
            groups[key].append(word)
        return list[groups.values()]