#!/usr/bin/env python3
# -*- coding: cp1252 -*-

# [Medium]
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def serialize(root):

    # def deserialize(s):

node = Node('root', Node('left', Node('left.left')), Node('right'))

# Layer 1
# node = Node('root', None, None)

# Layer 2
# node.left = Node('left', None, None)
# node.right = Node('right', None, None)

# Layer 3
# node.left.left = Node('left.left', None, None)

# tree node looks like:
#
#        root
#        /  \
#     left  right
#     /
#  left.left
#

# assert deserialize(serialize(node)).left.left.val == 'left.left'

