# cook your dish here

## cab rides
# t = int(input())
# while t > 0:
#     t -= 1
#     a = int(input())
#     cost = 0
#     for i in range(a):
#         if a <= 2 and a > 0:
#             cost = 200
#             break
#         elif a > 2:
#             cost = a*100
#             break
#     print(cost)
    
    

## orbs count
# R, B = map(int, input().split())
# diff = abs(R-B)
# print(diff)


# Passing Grade
# cook your dish here
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    
    chef_marks = a[0]
    passing_count = 0
    for i in range(n):
        if a[i] >= chef_marks:
            passing_count += 1
    print(passing_count)