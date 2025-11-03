# 1)Write a Python program to find the first non-repeating character in a given string.

# programming -> p
# aabbcdeeff -> c

from collections import Counter
def first_non_repeating_character(s):
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

print(first_non_repeating_character("Himanshu"))