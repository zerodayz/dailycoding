# Bubble Sort


def bubble_sort(l):
    print(l, "Original array")
    for i in range(0, len(l) - 1):
        for j in range(0, len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
        print(l, i)
    return l


array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
bubble_sort(array)
