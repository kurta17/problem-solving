class MinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.heap = [0]*self.max_size

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, element):
        if self.size >= self.max_size:
            return
        self.size += 1
        i = self.size - 1
        self.heap[i] = element
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def min_heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i
        if left < self.size and self.heap[left] < self.heap[i]:
            smallest = left
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def extract_min(self):
        if self.size == 0:
            return float('inf')
        root = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.min_heapify(0)
        return root


