orig = [1,1,2,3,4,4,5,5,5,6,7,8,8,9]
# def unique_num(arr):
#     unique = []
#     for i in arr:
#         if i not in unique:
#             unique.append(i)
#     return unique
# print("Unique numbers in the array:", unique_num(orig))

def unique_num(arr):
    uniq_xor = 0
    for i in range(1, max(arr)+1):
        uniq_xor ^= i

    full_xor = 0
    for num in arr:
        full_xor ^= num

    return uniq_xor ^ full_xor