## Hashing Technique in Python(For integer numbers)

'''# Read size of array
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
    q -= 1'''
    
    
    

##### Hashing Technique #####
# constraints -> 1<=n<=10, n and m values could be 10**8

# using list
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,6,7,2]

hash_list = [0]*(len(n)+1)

# Iterating 1st list
for num in n:
    hash_list[num]+=1

# Iterating 2nd list
for num in m:
    if num<1 or num>10:
        print(0)
    else:
        print(hash_list[num])




# Hashing - Dict
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,6,7,2]
hash_dict = {}

for num in n:
    if num in hash_dict:
        hash_dict[num]+=1
    else:
        hash_dict[num]=1

for num in m:
    print(hash_dict.get(num, 0))


# 2nd Method of dict
hash_dict = {}
for num in n:
    hash_dict[num] = hash_dict.get(num, 0) + 1
print(hash_dict)



# charcter Hashing 
s = "programming"
hash_dict1 = {}
for ch in s:
    hash_dict1[ch]=hash_dict1.get(ch, 0) + 1
print(hash_dict1)

