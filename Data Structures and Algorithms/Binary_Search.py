# Binary Search using iterative solution of two loops


def binary_search(input_array, value):
    print("looking for index of value:", value)
    print("in list:", input_array)

    step = 1
    original_list = input_array

    for j in range(0, round(len(input_array) / 2)):

        print("==== STEP", step, "====")

        left, right = [], []
        step += 1

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
            return original_list.index(value)
        elif value == left[0] and len(left) == 1:
            return original_list.index(value)
    return -1

test_list = [1,2,3,4,5,6,7,8,9]
test_val1 = 5
print(binary_search(test_list, test_val1))
