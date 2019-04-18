my_list = [1, (2,3), 4]
if 2 in my_list:
    print("2 is in list my_list")
else:
    print("2 is not in my_list")

my_list3 = list(range(5))
print(my_list3)

print("".join(['h','e','l','l','o']))
print("".join(('h','e','l','l','o')))
try:
    print("".join("h","e","l","l","o"))
except TypeError:
    print("TypeError: Too many arguments")

print("".join("h"))

my_list4 = []
my_list4 += "python"
print(my_list4)

# a is list while *a is expanded
a = [1, 2]
print(a, *a)

# Slicing list from the end
b = [1, 2, 3, 4]
print(b[-3:-1])

# Sorting
my_list5 = [1, 3, "a", 5]
try:
    print(my_list5.sort())
except TypeError:
    pass