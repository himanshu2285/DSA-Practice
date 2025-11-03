# Find maximum in an Array

# for T in range(int(input())):
#     N = int(input())
#     arr = []
#     for i in range(N):
#         arr.append(int(input()))
#     print(max(arr))
    
    
for T in range(int(input())):
    N = int(input())
    arr = [int(x) for x in input().split()]
    print(max(arr))