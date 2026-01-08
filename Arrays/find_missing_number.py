'''Find the Missing Number in an Array a of length n'''

# Given:
a = [3, 1, 4, 5]
n = 5


# 1st approach: Gauss Code (Here we find sum of n natural numbers with the formula n(n+1)/2) = 5(5+1)/2 = 15
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


# 3rd approach:

# A = [3,1,4,5]
# N = 5
# class Solution:
#     def find_number(self, A, N):
#         missing_value = None
#         for num in range(1, N+1):
#             if num not in A:
#                 missing_value = num
#                 break
#         return f"Missing number is {missing_value}"
        
# obj = Solution()
# print(obj.find_number(A, N))