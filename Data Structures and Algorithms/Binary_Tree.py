# Binary Tree


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """
        BFS - Level Order (Check out first everything on the same level)
        DFS - Pre-order traversal (Check out nodes as we visit them)
        DFS - In-order traversal (Check out left child - starting with leafs)
        DFS - Post-order traversal (Check out parents only after childs are checked out- starting with leafs
        """
        current = self.root
        self.preorder_search(current, find_val)

    def print_tree(self):
        current = self.root
        traversal = []

        self.preorder_print(current, traversal)
        return "-".join(str(t) for t in traversal)

    def preorder_search(self, current, find_val):
        if not current:
            return ""

        self.preorder_search(current.left, find_val)
        self.preorder_search(current.right, find_val)

    def preorder_print(self, current, traversal):
        if not current:
            return ""

        traversal.append(current.value)
        self.preorder_print(current.left, traversal)
        self.preorder_print(current.right, traversal)

        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# tree node looks like:
#
#         1
#        /  \
#       2    3
#      / \
#     4   5
#


# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(5)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()