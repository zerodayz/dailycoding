import itertools

t = itertools.count(1, 2)
list1 = []

# 1, 5, 9
while next(t) < 10:
    # 3, 7, 11
    list1.append(next(t))

print(list1)