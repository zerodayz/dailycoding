# Quick Sort


def quick_sort(l):
    quick_sort_helper(l, len(l) - 1, 0)
    return l


def quick_sort_helper(l, pivot, counter):
    if counter < pivot:
        p = divide(l, pivot, counter)
        quick_sort_helper(l, p - 1, counter)
        quick_sort_helper(l, pivot, p + 1)


def divide(l, pivot, counter):

    while counter != pivot:
        if l[counter] > l[pivot] and pivot - 1 != counter:
            l[pivot], l[pivot-1] = l[pivot-1], l[pivot]
            l[counter], l[pivot] = l[pivot], l[counter]
            pivot -= 1
        elif l[counter] > l[pivot] and pivot - 1 == counter:
            l[pivot], l[pivot - 1] = l[pivot - 1], l[pivot]
            pivot -= 1
        elif l[counter] == l[pivot]:
            pivot -= 1
        elif l[counter] < l[pivot]:
            counter += 1

    return pivot


array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quick_sort(array))
