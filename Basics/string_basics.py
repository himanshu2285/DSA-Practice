# string_basics.py
# Basic Python String Programs for Beginners

# 1. Print a string
print("1. Print a string:")
s = "Hello World"
print(s)
print()

# 2. Find length of string
print("2. Length of string:")
print(len(s))
print()

# 3. Convert to uppercase and lowercase
print("3. Uppercase and Lowercase:")
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print()

# 4. String concatenation
print("4. String Concatenation:")
a = "Hello"
b = "Python"
print(a + " " + b)
print()

# 5. Check substring in string
print("5. Check substring:")
text = "I am learning Python"
print("Python" in text)
print()

# 6. Reverse a string
print("6. Reverse a string:")
rev = s[::-1]
print(rev)
print()

# 7. Count characters
print("7. Count occurrence of character:")
print("Number of l:", s.count('l'))
print()

# 8. Replace substring
print("8. Replace substring:")
print(s.replace("World", "Python"))
print()

# 9. Split string
print("9. Split string:")
data = "apple,banana,mango"
print(data.split(","))
print()

# 10. Remove spaces using strip
print("10. Remove spaces:")
name = "   Himanshu   "
print(name.strip())
print()
