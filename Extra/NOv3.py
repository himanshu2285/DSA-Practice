# 2) Remove characters from first string that are present in second string

def remove_char(str1, str2):
    return ''.join(char for char in str1 if char not in str2)

print(remove_char("abcdefg", "bdg"))



# 3) Reverse words in a given string
words = "Hello World from Python"
reversed_words = ' '.join(reversed(words.split()))
print(reversed_words)


arr = [2,4,5,6,1,4,6]
arr.sort()
print(arr)



# 4) Binary Search Implementation
def binary_search(arr, target):
    low=0
    high=len(arr)-1
    
    while low <= high:
        mid = low + (high - low) // 2
        if  arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr1 = [12,23,34,45,56,67,77,88,90,91,93,95]
targ = 8
result = binary_search(arr1, targ)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")