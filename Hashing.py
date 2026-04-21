## Hashing Technique in Python(For integer numbers)

# Read size of array
n = int(input())
# Read array elements
arr = list(map(int, input().split()))

# Precompute frequency (hash array)
hash_arr = [0] * 13

for i in range(n):
    hash_arr[arr[i]] += 1

# Read number of queries
q = int(input())
print("Query results:")

# Process each query
while q > 0:
    number = int(input())
    print(number, "->", hash_arr[number])
    q -= 1
    
    
    
## Hashing Technique in Python(For string)
