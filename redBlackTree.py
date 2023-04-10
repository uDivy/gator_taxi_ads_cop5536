"""
This code defines a Red-Black Tree data structure, which is a self-balancing binary search tree 
                                                            with the following properties:

Every node is colored either red or black.
The root node is always black.
Every leaf node is black.
If a node is red, then both its children must be black.
Every path from a node to a descendant leaf node contains the same number of black nodes.
The class Node represents a node in the tree, with a key attribute, a value attribute 
                                (which is optional), and references to its left and right children nodes. 
                                It also has a color attribute, which defaults to "RED" if not specified.
The class RedBlackTree represents the tree itself, with a root attribute that holds the root node of the tree.
"""

class Node:
    def __init__(self, key, value=None, color="RED"):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = color
        
class RedBlackTree:
    def __init__(self):
        self.root = None

    def is_red(self, node):
        # returns True if the given node is red, False otherwise.
        if not node:
            return False
        return node.color == "RED"

    def rotate_left(self, node):
        # performs a left rotation on the given node and its right child, and returns the new root of the subtree.
        right = node.right
        node.right = right.left
        right.left = node
        right.color = node.color
        node.color = "RED"
        return right

    def rotate_right(self, node):
        # performs a right rotation on the given node and its left child, and returns the new root of the subtree.
        left = node.left
        node.left = left.right
        left.right = node
        left.color = node.color
        node.color = "RED"
        return left

    def flip_colors(self, node):
        # flips the colors of the given node and its two children.
        node.color = "RED"
        node.left.color = "BLACK"
        node.right.color = "BLACK"

    def put(self, key, value=None):
        """
        inserts a new node with the given key and value (if specified) into the tree. 
        If the key already exists in the tree, its value is updated.
        """
        self.root = self._put(self.root, key, value)
        self.root.color = "BLACK"

    def _put(self, node, key, value=None):
        # is a helper function for put() that inserts a new node into the subtree rooted at the given node.
        if not node:
            return Node(key, value)

        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        return node

    def get(self, key):
        # returns the value associated with the given key in the tree, or None if the key is not found.
        node = self.root
        while node:
            if key == node.key:
                return node.value
            elif key < node.key:
                node = node.left
            else:
                node = node.right

        return None

    def delete(self, key):
        # removes the node with the given key from the tree.
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        # is a helper function for delete() that removes the node with the given key from the subtree rooted at the given node.
        if not node:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                successor = self._get_min(node.right)
                node.key = successor.key
                node.value = successor.value
                node.right = self._delete(node.right, successor.key)

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        return node

    def _get_min(self, node):
        # returns the node with the minimum key in the subtree rooted at the given node.
        while node.left:
            node = node.left
        return node