#!/usr/bin/env python3
# -*- coding: cp1252 -*-

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

mylist = [10, 15, 11, 5]
k = 16

# Brute force method where we compare each number with other numbers in mylist


def list_sum_two_iter(l, n):
    for i in range(len(l)):
        print("Processing number at position i: ", i)
        print(l[i])
        for j in range(len(l)):
            if i == j:
                pass
            elif l[i] + l[j] == n:
                print("Found number ", l[i], " + ", l[j], " is ", n, ".")
                return True



if list_sum_two_iter(mylist, k):
    print("Any two numbers of ", mylist, " adds up to ", k)
else:
    print("No two numbers of the list ", mylist, " adds up to ", k)