#!/usr/bin/env python3
# -*- coding: cp1252 -*-

import time
import random

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# mylist = [10, 15, 11, 5, 20]
# sortedMylist = [5, 10, 11, 15, 20]
# k = 30
n = 1000000


def generate_input(n):
    start = time.time()
    randomlist = [None] * n
    for i in range(0, len(randomlist)):
        randomlist[i] = random.randint(1, n)
    sortedrandomlist = sorted(randomlist)
    randomnumber = random.randint(1, n)
    end = time.time()
    print("Elapsed time: ", end - start)
    return randomnumber, randomlist, sortedrandomlist

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
                return True, l[i], l[j]

# Fast method (required sorted list) doesn't require two for loops


def list_sum_linear(l,n):
    start = time.time()
    high_val_index = len(l)-1
    low_val_index = 0

    while low_val_index != high_val_index:
        if l[low_val_index] + l[high_val_index] == n:
            end = time.time()
            print("Elapsed time: ", end - start)
            return True, l[low_val_index], l[high_val_index]
        elif l[low_val_index] + l[high_val_index] > n:
            high_val_index -= 1
        elif l[low_val_index] + l[high_val_index] < n:
            low_val_index += 1
    return False


print("==================STEP 1==========================")
print("Generating input list with ", n, "items.")

randomnumber, randomlist, sortedrandomlist = generate_input(n)

print("==================STEP 2==========================")
print("Searching for two numbers using linear method that adds up to ", randomnumber, " within ", n, "items.")

boolean, n1, n2 = list_sum_linear(sortedrandomlist, randomnumber)

if boolean is True:
    # print(sortedrandomlist)
    print("list_sum_linear: Found ", n1, " and ", n2, " adds up to ", randomnumber)
else:
    print("list_sum_linear: No two numbers found that adds up to ", randomnumber)

print("==================STEP 3==========================")
print("Searching for two numbers using iterating method that adds up to ", randomnumber, " within ", n, "items.")

boolean, n1, n2 = list_sum_two_iter(randomlist, randomnumber)

if boolean is True:
    # print(randomlist)
    print("list_sum_two_iter: Found ", n1, " and ", n2, " adds up to ", randomnumber)
else:
    print("list_sum_two_iter: No two numbers found that adds up to ", randomnumber)
