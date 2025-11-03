
# Take discount or Not




# t = int(input())

# while t > 0:
#     n, x, y = map(int, input().split())
#     a = list(map(int, input().split()))
#     t -= 1
#     # Your code goes here
    
#     sum_of_items = sum(a)
#     for i in range(n):
#         coupon_sum = x + (a[i] - y)
#         if coupon_sum < sum_of_items:
#             coupon = True
#         else:
#             coupon = False

#     if coupon == True:
#         print("COUPON")
#     else:
#         print("NO COUPON")


def solution():
    N, X, Y = map(int, input().split())
    A= list(map(int, input().split()))
    
    total = sum(A)
    total_with_discount = X

    for a in A:
        total_with_discount += max(a - Y, 0)
    if total > total_with_discount:
        print("COUPON")
    else:
        print("NO COUPON")
        
T = int(input())
while T > 0:
    T = T - 1
    solution()
    



