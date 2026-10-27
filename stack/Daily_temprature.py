class Solution:
    def DT(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
                
            stack.append(i)
        return result

obj = Solution()
print(obj.DT([73,74,75,71,69,72,76,73]))
print(obj.DT([30,40,50,60]))
print(obj.DT([30,60,90]))