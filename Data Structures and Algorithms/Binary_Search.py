# Binary Search using iterative solution of two loops


def binary_search(input_array, value):
    print("looking for value:", value)

    for j in range(0, round(len(input_array) / 2)):
        left, right = [], []

        for i in range(0, len(input_array)):
            if i < len(input_array) / 2:
                left.append(input_array[i])
            elif i >= len(input_array) / 2:
                right.append(input_array[i])

        print("left: ", left)
        print("right: ", right)

        if value > left[-1] and len(right) > 1:
            print("value not found in left, trying right.")
            input_array = right
        elif value < right[0] and len(left) > 1:
            print("value not found in right, trying left.")
            input_array = left

        if value == right[0] and len(right) == 1:
            return value
        elif value == left[0] and len(left) == 1:
            return value
    return -1

test_list = [1,2,3,4,5,6,7,8,9]
test_val1 = 9
test_val2 = 12
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))