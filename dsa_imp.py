###### 1. Hashing #####
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m=[10,111,1,9,5,6,7,2]

# 1st way - List (When the data is finite)
'''hash_list = [0]*(len(n)+1)
for num in n:
    hash_list[num]+=1
for num in m:
    if num<1 or num>10:
        print(0)
    else:
        print(hash_list[num])'''
        

# 2nd way - Dictionary (When when values can be large, negative, strings, or unknown.)
'''hash_dict = {}
for num in n:
    hash_dict[num]=hash_dict.get(num, 0) + 1
print(hash_dict)'''

# For string 
'''s = 'programming'
hash_dict = {}
for ch in s:
    hash_dict[ch] = hash_dict.get(ch, 0) + 1
print(hash_dict)'''


# 268. Missing Number
# nums = [3,0,1]
# nums = [0,1]
# nums = [9,6,4,2,3,5,7,0,1]
nums = [1]

nums.sort()
def missing_number(nums):
    for i in range(len(nums)):
        if nums[i]!=i:
            return i
    return len(nums)
print(missing_number(nums))
    