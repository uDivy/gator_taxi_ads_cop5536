class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, node):
        if not self.heap:
            self.heap.append(node)
        else:
            self.heap.append(node)
            self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            min_node = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._bubble_down(0)
            return min_node

    def _bubble_up(self, node):
        idx = self.heap.index(node)
        parent_idx = (idx - 1) // 2
        if parent_idx < 0:
            return
        if self.heap[parent_idx].tripDuration > node.tripDuration:
            self.heap[parent_idx], node = node, self.heap[parent_idx]
            self._bubble_up(node)

    def _bubble_down(self, idx):
        left_child_idx = idx * 2 + 1
        right_child_idx = idx * 2 + 2
        min_idx = idx
        if left_child_idx < len(self.heap) and self.heap[left_child_idx].tripDuration < self.heap[min_idx].tripDuration:
            min_idx = left_child_idx
        if right_child_idx < len(self.heap) and self.heap[right_child_idx].tripDuration < self.heap[min_idx].tripDuration:
            min_idx = right_child_idx
        if min_idx != idx:
            self.heap[idx], self.heap[min_idx] = self.heap[min_idx], self.heap[idx]
            self._bubble_down(min_idx)

    def is_empty(self):
        return len(self.heap) == 0

    def decrease_key(self, node):
        self._bubble_up(node)