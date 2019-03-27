# Quick Sort


def quick_sort(l):
    pivot = len(l) - 1
    counter = 0
    while counter != pivot:
        if l[counter] > l[pivot]:
            l[pivot], l[pivot-1] = l[pivot-1], l[pivot]
            l[counter], l[pivot] = l[pivot], l[counter]
            pivot -= 1
        elif l[counter] < l[pivot]:
            counter += 1

    return l

# TODO: This is first part

array = [8, 3, 1, 7, 0, 10, 2]
print(quick_sort(array))
