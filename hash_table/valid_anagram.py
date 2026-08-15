class Solution:
    def anagram(self, s:str, t:str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            count_freq={}
            for ch in s:
                count_freq[ch] = count_freq.get(ch, 0) + 1
            for ch in t:
                if ch not in count_freq:
                    return False
                else:
                    if count_freq[ch]==0:
                        return False
                    else:
                        count_freq[ch]-=1
            return True