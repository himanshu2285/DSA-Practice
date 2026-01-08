n = 89746
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

print("Number of digits:", count_digits(n))

# TC: O(log10 n)
# SC: O(1)