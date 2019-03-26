# Merge Sort


def merge_sort(list):
    if len(list) == 1:
        return list

    number_of_elements = round(len(list) / 2)

    left_array = list[:number_of_elements]
    right_array = list[number_of_elements:]

    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)

    return merge(left_array, right_array)


def merge(left_array, right_array):
    new_list = []

    while len(left_array) > 0 and len(right_array) > 0:
        if left_array[0] > right_array[0]:
            new_list.append(right_array[0])
            right_array.pop(0)
        elif right_array[0] > left_array[0]:
            new_list.append(left_array[0])
            left_array.pop(0)

    while len(left_array) > 0:
        new_list.append(left_array[0])
        left_array.pop(0)

    while len(right_array) > 0:
        new_list.append(right_array[0])
        right_array.pop(0)

    return new_list


array = [21, 4, 1, 3, 9, 20, 25]
print(array, "Original array")
print(merge_sort(array))
