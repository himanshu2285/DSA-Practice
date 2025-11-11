
# Sort an array without using built-in functions

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Sorted array:", arr)