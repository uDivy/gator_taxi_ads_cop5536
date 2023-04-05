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

    # def delete(self, key):
    #     self.root = self._delete(self.root, key)

    # def _delete(self, node, key):
    #     if not node:
    #         return None

    #     if key < node.key:
    #         node.left = self._delete(node.left, key)
    #     elif key > node.key:
    #         node.right = self._delete(node.right, key)
    #     else:
    #         if not node.right:
    #             return node.left
    #         elif not node.left:
    #             return node.right
    #         else:
    #             temp = node
    #             node = self._delete_min(temp.right)
    #             node.right = self._delete_min(temp.right)
    #             node.left = temp.left

    #     if self.is_red(node.right) and not self.is_red(node.left):
    #         node = self.rotate_left(node)
    #     if self.is_red(node.left) and self.is_red(node.left.left):
    #         node = self.rotate_right(node)
    #     if self.is_red(node.left) and self.is_red(node.right):
    #         self.flip_colors(node)

    #     return node

    # def delete_min(self):
    #     self.root = self._delete_min(self.root)

    # def _delete_min(self, node):
    #     if not node.left:
    #         return node.right

    #     if not self.is_red(node.left) and not self.is_red(node.left.left):
    #         node = self.move_red_left(node)

    #     node.left = self._delete_min(node.left)

    #     return self.balance(node)

    def _delete(self, node, key):
        if not node:
            return node

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
                temp = node
                node = self._delete_min(temp.right)
                node.right = self._delete_min(temp.right)
                node.left = temp.left

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        return node

    def _delete_min(self, node):
        if not node.left:
            return node.right

        node.left = self._delete_min(node.left)

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)
        if self.root:
            self.root.color = "BLACK"


















            class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        elif len(self.heap) > 1:
            min_val = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._bubble_down(0)
            return min_val

    def _bubble_up(self, idx):
        parent_idx = (idx - 1) // 2
        if parent_idx < 0:
            return
        if self.heap[parent_idx] > self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            self._bubble_up(parent_idx)

    def _bubble_down(self, idx):
        left_child_idx = idx * 2 + 1
        right_child_idx = idx * 2 + 2
        min_idx = idx
        if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[min_idx]:
            min_idx = left_child_idx
        if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[min_idx]:
            min_idx = right_child_idx
        if min_idx != idx:
            self.heap[idx], self.heap[min_idx] = self.heap[min_idx], self.heap[idx]
            self._bubble_down(min_idx)

    def is_empty(self):
        if len(self.heap) == 0:
            return True
        else:
            return False