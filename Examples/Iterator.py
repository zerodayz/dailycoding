import itertools

def functionA(x):
    return x <= 3

t = itertools.count(1, 2)
list1 = []

# 1, 5, 9
while next(t) < 10:
    # 3, 7, 11
    list1.append(next(t))

print(list1)

list2 = [1,8, 2, 4]
t1 = itertools.cycle(list2)
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))

# add all previous values to current value
t2 = itertools.accumulate(list2)
print(list(t2))

# loops thru the list and pins to the largest number
t2 = itertools.accumulate(list2, max)
print(list(t2))

t3 = itertools.chain("Red","Hat")
print(list(t3))

numbers = [0, 1, 2, 4, 5, 7]
t4 = itertools.dropwhile(functionA, numbers)
print(list(t4))

t5 = itertools.takewhile(functionA, numbers)
print(list(t5))