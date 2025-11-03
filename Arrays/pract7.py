
# Largest and Second Largest

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    
    a.sort()
    ans = 0
    for i in reversed(range(n)):
        if a[i] == a[-1]:
            continue
        ans = a[i]+a[-1]
        break
    print(ans)