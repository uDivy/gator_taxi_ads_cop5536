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
        if not node:
            return False
        return node.color == "RED"

    def rotate_left(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        right.color = node.color
        node.color = "RED"
        return right

    def rotate_right(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        left.color = node.color
        node.color = "RED"
        return left

    def flip_colors(self, node):
        node.color = "RED"
        node.left.color = "BLACK"
        node.right.color = "BLACK"

    def put(self, key, value=None):
        self.root = self._put(self.root, key, value)
        self.root.color = "BLACK"

    def _put(self, node, key, value=None):
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
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
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
        while node.left:
            node = node.left
        return node