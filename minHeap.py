class MinHeap:
    def __init__(self):
        """
        Initializes an empty heap with a single None value as the first element of the list 
        to ensure that the indexing starts at 1 instead of 0, which simplifies the implementation 
        of the heap.
        """
        self.heap = [None]
    
    def insert(self, node):
        """
        Inserts a new node into the heap and restores the heap property by calling the _bubble_up() function.
        """
        self.heap.append(node)
        self._bubble_up(len(self.heap) - 1)
    
    def _bubble_up(self, idx):
        """
        Restores the heap property by swapping the node at position idx with its parent as long as 
        its parent has a higher ride cost or the same ride cost but a longer trip duration. 
        This function recursively calls itself until the heap property is restored.
        """
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
        """
        Removes and returns the node with the lowest ride cost and the shortest trip duration 
        from the heap, which is the root node of the heap. The function restores the heap property 
        by calling the _bubble_down() function after replacing the root node with the last node 
        in the heap.
        """
        if len(self.heap) == 1:
            return None
        min_val = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self._bubble_down(1)
        return min_val
    
    def _bubble_down(self, idx):
        """
        Restores the heap property by swapping the node at position idx with its smallest child 
        if the child has a lower ride cost or the same ride cost but a shorter trip duration. 
        This function recursively calls itself until the heap property is restored.
        """
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
        """
        Restores the heap property after the ride cost or trip duration of a node is 
        decreased by calling the _bubble_up() function with the index of the node in the heap.
        """
        idx = self.heap.index(node)
        self._bubble_up(idx)
    
    def delete(self, node):
        """
        Removes a node from the heap and restores the heap property by calling both the 
        _bubble_up() and _bubble_down() functions with the index of the node in the heap.
        """
        idx = self.heap.index(node)
        self.heap[idx] = self.heap[-1]
        self.heap.pop()
        if idx < len(self.heap):
            self._bubble_up(idx)
            self._bubble_down(idx)
    
    def is_empty(self):
        """
        Returns True if the heap only contains the None value and False otherwise.
        """
        return len(self.heap) == 1