
#Running Comparison Operators on Arrays

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
   
    # Your code goes here
    
    happy_count = 0
    for i in range(n):
        if a[i] <= 2*b[i] and b[i] <= 2*a[i]:
            happy_count += 1
        
    print(happy_count)
    t -= 1