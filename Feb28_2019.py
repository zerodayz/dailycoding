#!/usr/bin/env python3
# -*- coding: cp1252 -*-

# [Hard]
# Given an array of integers, return a new array such that each element at index i of
# the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

input_list = [1, 2, 3, 4, 5]
output_list = []


def multiply(il):
    for i in range(len(il)):
        r = 1
        for j in range(len(il)):
            if j == i:
                pass
            else:
                r = r * il[j]
        output_list.append(r)
    return output_list


print(multiply(input_list))


#    1, 2, 3, 4, 5
#    2*3*4*5 = 120
#    1*3*4*5 = 60
#    1*2*4*5 = 40
#    1*2*3*5 = 30
#    1*2*3*4 = 24
