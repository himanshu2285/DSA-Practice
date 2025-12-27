'''Find the Missing Number in an Array of length n'''

# Given:
a = [3, 1, 4, 5]
n = 5


# 1st approach: Gauss Code (Here we find n natural numbers with the formula n(n+1)/2)
class Solution:
    def find_missing_number_gauss(self, arr, n):
        expected_sum = n * (n + 1) // 2
        actual = 0
        for num in arr:
            actual += num
        return expected_sum - actual
    
obj = Solution()
print(obj.find_missing_number_gauss(a, n))

# 2nd approach: Using XOR operation
class Solution2:
    def find_missing_number_xor(self, arr, n):
        xor_full = 0
        xor_arr = 0
        
        for i in range(1, n + 1):
            xor_full ^= i
            
        for num in arr:
            xor_arr ^= num
            
        return xor_full ^ xor_arr
    
obj1 = Solution2()
print(obj1.find_missing_number_xor(a, n))