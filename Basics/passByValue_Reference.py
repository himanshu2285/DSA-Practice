# pass by reference example
def fun(x):
    x = x + 10
a = 5
fun(a)
print(a)
# Here int is immutable, so the original value of 'a' remains unchanged.


# pass by value example
def add_element(lst):
    lst.append(4)
my_list = [1, 2, 3]
add_element(my_list)
print(my_list)
# Here list is mutable, so the original list is modified.