class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for ch in s:
            if ch in '({[': # push operation (for open bracket)
                stack.append(ch)
            else:           # pop operation (for close bracket)
                if not stack: # if stack has only close bracket ("]")
                    return False
                if stack[-1]!=pairs[ch]:
                    return False
                stack.pop()
        return len(stack)==0
        