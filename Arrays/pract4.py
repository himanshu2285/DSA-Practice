
#Find groceries cost

t = int(input())

while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))  # frshness value
    b = list(map(int, input().split()))  # cost of item
    # Your code goes here
    t -= 1
    cost = 0

    for i in range(len(b)):
        if a[i] >= x:
            cost += b[i]
        else:
            continue
    print(cost)
    