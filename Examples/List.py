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

try:
    dictionary = {0,1,2,3,4}
    x = dictionary[len(dictionary) - 1]
    y = x % 4
    print(y)
except TypeError:
    pass

dictionary2 = {'r':'e','d':'h','a':'t'}
print(len(dictionary2))

my_list2 = ['ac','dc']
for i in my_list2:
    print(i.upper())
print(my_list2)

print("0" or "1")
print("1" and "2")

a, b, *c = [1, 2, 3, 4]
print(c)
print(*c)

x, y = 0, int(True)
x = x + 1
y = int(True)
b = 2
b_list = [2]
c = 2
c_list = [2]
print(id(b))
print(id(c))
print(id(b_list))
print(id(c_list))
print(id(x) == id(y))