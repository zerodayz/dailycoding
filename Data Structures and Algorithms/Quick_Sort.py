# Quick Sort


def quick_sort(l):
    if len(l) < 2:
        return

    counter = 0
    pivot = len(l) - 1
    pivot = divide(l, counter, pivot)

    return l


def divide(l, counter, pivot):

    while counter != pivot:
        if l[counter] > l[pivot] and pivot - 1 != counter:
            l[pivot], l[pivot-1] = l[pivot-1], l[pivot]
            l[counter], l[pivot] = l[pivot], l[counter]
            pivot -= 1
        elif l[counter] > l[pivot] and pivot - 1 == counter:
            l[pivot], l[pivot - 1] = l[pivot - 1], l[pivot]
        elif l[counter] < l[pivot]:
            counter += 1

    return pivot

# TODO: This is first part


array = [8, 3, 1, 7, 0, 10, 2]
print(quick_sort(array))
