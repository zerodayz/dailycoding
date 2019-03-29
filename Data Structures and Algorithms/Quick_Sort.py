# Quick Sort


def quick_sort(l):
    quick_sort_helper(l, len(l) - 1, 0)


def quick_sort_helper(l, pivot, counter):
    if counter < pivot:
        pivot = divide(l, pivot, counter)
        quick_sort_helper(l, pivot - 1, counter)
        #quick_sort_helper(l, len(l) - 1, pivot + 2)
    return l


def divide(l, pivot, counter):

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
