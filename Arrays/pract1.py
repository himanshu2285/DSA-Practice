# Search an element in an array

N,X = map(int, input().split())

A = list(map(int, input().split()))

# [METHOD 1]

# found = False
# for i in range(N):
#     if A[i] == X:
#         found = True
#         print("YES")
#         break
# if not found:
#     print("NO")


# [METHOD 2]
if X in A:
    print("YES")
else:
    print("NO")