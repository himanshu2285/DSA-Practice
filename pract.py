

# Recursion to calculate factorial of a number
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
print(fact(1))