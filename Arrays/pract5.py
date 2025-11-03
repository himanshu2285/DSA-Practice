
# Count minimum number of operation to make min to maximum

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the size of the array
    n = int(input())
    
    # Read the array elements
    a = list(map(int, input().split()))
    
    # Find the minimum element
    minimum = a[0]
    for i in range(n):
        minimum = min(a[i], minimum)
    
    # Count the occurrences of the minimum element
    count = 0
    for i in range(n):
        if a[i] == minimum:
            count += 1
    
    # Print the result
    print(n - count)