# Binary Search Tree #1 First attempt


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current = self.root
        self.insert_helper(new_val, current)
    
    def insert_helper(self, new_val, current):
        if current.left is None and new_val < current.value:
            current.left = Node(new_val)
            return True
        elif current.right is None and new_val > current.value:
            current.right = Node(new_val)
            return True

        if new_val > current.value:
            current = current.right
            self.insert_helper(new_val, current)
        elif new_val < current.value:
            current = current.left
            self.insert_helper(new_val, current)

    def search(self, find_val):
        current = self.root
        while current:
            if find_val == current.value:
                return True
            elif find_val > current.value:
                current = current.left
            elif find_val < current.value:
                current = current.right
        return False


# Set up tree
tree = BinarySearchTree(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# tree node looks like:
#
#         4
#        /  \
#       2    5
#      / \
#     1   3
#


# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))