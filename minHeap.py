class MinHeap:
    def __init__(self):
        self.heap = [None]
    
    def insert(self, node):
        self.heap.append(node)
        self._bubble_up(len(self.heap) - 1)
    
    def _bubble_up(self, idx):
        if idx <= 1:
            return
        parent_idx = idx // 2
        if self.heap[parent_idx].rideCost > self.heap[idx].rideCost:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            self._bubble_up(parent_idx)
        elif self.heap[parent_idx].rideCost == self.heap[idx].rideCost and self.heap[parent_idx].tripDuration > self.heap[idx].tripDuration:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            self._bubble_up(parent_idx)
    
    def extract_min(self):
        if len(self.heap) == 1:
            return None
        min_val = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self._bubble_down(1)
        return min_val
    
    def _bubble_down(self, idx):
        left_idx = 2 * idx
        right_idx = 2 * idx + 1
        min_idx = idx
        if left_idx < len(self.heap) and self.heap[left_idx].rideCost < self.heap[min_idx].rideCost:
            min_idx = left_idx
        elif left_idx < len(self.heap) and self.heap[left_idx].rideCost == self.heap[min_idx].rideCost and self.heap[left_idx].tripDuration < self.heap[min_idx].tripDuration:
            min_idx = left_idx
        if right_idx < len(self.heap) and self.heap[right_idx].rideCost < self.heap[min_idx].rideCost:
            min_idx = right_idx
        elif right_idx < len(self.heap) and self.heap[right_idx].rideCost == self.heap[min_idx].rideCost and self.heap[right_idx].tripDuration < self.heap[min_idx].tripDuration:
            min_idx = right_idx
        if min_idx != idx:
            self.heap[min_idx], self.heap[idx] = self.heap[idx], self.heap[min_idx]
            self._bubble_down(min_idx)
    
    def decrease_key(self, node):
        idx = self.heap.index(node)
        self._bubble_up(idx)
    
    def delete(self, node):
        idx = self.heap.index(node)
        self.heap[idx] = self.heap[-1]
        self.heap.pop()
        if idx < len(self.heap):
            self._bubble_up(idx)
            self._bubble_down(idx)
    
    def is_empty(self):
        return len(self.heap) == 1


# class MinHeap:
#     def __init__(self):
#         self.heap = [None]
    
#     def insert(self, node):
#         self.heap.append(node)
#         self._bubble_up(len(self.heap) - 1)
    
#     def _bubble_up(self, idx):
#         if idx <= 1:
#             return
#         parent_idx = idx // 2
#         if self.heap[parent_idx] > self.heap[idx]:
#             self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
#             self._bubble_up(parent_idx)
    
#     def extract_min(self):
#         if len(self.heap) == 1:
#             return None
#         min_val = self.heap[1]
#         self.heap[1] = self.heap[-1]
#         self.heap.pop()
#         self._bubble_down(1)
#         return min_val
    
#     def _bubble_down(self, idx):
#         left_idx = 2 * idx
#         right_idx = 2 * idx + 1
#         min_idx = idx
#         if left_idx < len(self.heap) and self.heap[left_idx] < self.heap[min_idx]:
#             min_idx = left_idx
#         if right_idx < len(self.heap) and self.heap[right_idx] < self.heap[min_idx]:
#             min_idx = right_idx
#         if min_idx != idx:
#             self.heap[min_idx], self.heap[idx] = self.heap[idx], self.heap[min_idx]
#             self._bubble_down(min_idx)
    
#     def decrease_key(self, node):
#         idx = self.heap.index(node)
#         self._bubble_up(idx)
    
#     def delete(self, node):
#         idx = self.heap.index(node)
#         self.heap[idx] = self.heap[-1]
#         self.heap.pop()
#         if idx < len(self.heap):
#             self._bubble_up(idx)
#             self._bubble_down(idx)
    
#     def is_empty(self):
#         return len(self.heap) == 1