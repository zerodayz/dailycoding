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

my_list6 = [1, 2, [3, 4]]
print(my_list6[2][0])

a = 12
b = a
a = 10
print(b)
del(a)
print(b)

a = [12, 11]
b = a
a[0] = 10
print(b)
del(a[0])
print(b)

x = [[0],[1]]
print(list(map(str,x)))
print(' '.join(list(map(str,x))))
print(len(' '.join(list(map(str,x)))))

a = [1,2,3]
for a[-1] in a:
    print(a[-1])

a = (8,-1,3)
try:
    a.sort()
except Exception:
    pass

print(a[0])

a = [5, 6, 3]
b = a
b[0] = 2
print(a)

def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(sum(1, 2, 3, 4, 5))
print(sum(1, 2, 3))
print(sum(*a))

print(a)
print(b)
a = a.sort()
print(b)

dictionary = {0,3,2,4,3}
print(len(dictionary))

a = [[0] * 2] * 2
print(a)
a[0][0] = 1
print(a)
print(a[0][0] + a[1][0])