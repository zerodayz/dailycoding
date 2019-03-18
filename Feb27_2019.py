#!/usr/bin/env python3
# -*- coding: cp1252 -*-

import time

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

mylist = [10, 15, 11, 5, 20]
sortedMylist = [5, 10, 11, 15, 20]
k = 20

# Brute force method where we compare each number with other numbers in mylist
# Slow method


def list_sum_two_iter(l, n):
    start = time.time()
    for i in range(len(l)):
        # print("Processing number at position i: ", i)
        # print(l[i])
        for j in range(len(l)):
            if i == j:
                pass
            elif l[i] + l[j] == n:
                # print("Found number ", l[i], " + ", l[j], " is ", n, ".")
                end = time.time()
                print("Elapsed time: ", end - start)
                return True

# Fast method (required sorted list) doesn't require two for loops


def list_sum_linear(l,n):
    start = time.time()
    high_val_index = len(l)-1
    low_val_index = 0

    while low_val_index != high_val_index:
        if l[low_val_index] + l[high_val_index] == n:
            end = time.time()
            print("Elapsed time: ", end - start)
            return True
        elif l[low_val_index] + l[high_val_index] > n:
            high_val_index -= 1
        elif l[low_val_index] + l[high_val_index] < n:
            low_val_index += 1
    return False


if list_sum_linear(sortedMylist, k):
    print("list_sum_linear: Any two numbers of ", mylist, " adds up to ", k)
else:
    print("list_sum_linear: No two numbers of the list ", mylist, " adds up to ", k)

print("============================================")

if list_sum_two_iter(mylist, k):
    print("list_sum_two_iter: Any two numbers of ", mylist, " adds up to ", k)
else:
    print("list_sum_two_iter: No two numbers of the list ", mylist, " adds up to ", k)
