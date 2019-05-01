list1 = [0, 1, 2, 3, 4, 5, 6]
list2 = ["a", "b", "c", "d", "e"]
i = iter(list1)
print(next(i))
print(next(i))
print(next(i))

for i in range(len(list1)):
    print(i+1, list1[i])

for i,n in enumerate(list1, start=1):
    print(i, n)


for n in zip(list1, list2):
    print(n)

for i, n in enumerate(zip(list1, list2), start=1):
    print(i, n[0], n[1])