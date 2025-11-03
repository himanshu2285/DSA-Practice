# 2)Remove characters from first string that are present in second string

def remove_char(str1, str2):
    return ''.join(char for char in str1 if char not in str2)

a = input("Enter first string: ")
b = input("Enter second string: ")
print(remove_char(a, b))



# 3)Reverse words in a given string
words = "Hello World from Python"
reversed_words = ' '.join(reversed(words.split()))
print(reversed_words)