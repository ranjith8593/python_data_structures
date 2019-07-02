class Heap:
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def new_min_heap_node(self, value , dist):
        # dist from which node ?
        node = [value, dist]
        return node

    def swap_min_heap_node(self, a_loc , b_loc):
        temp = self.array[a_loc]
        self.array[a_loc] = self.array[b_loc]
        self.array[b_loc] = temp

    def min_heapify(self, index):
        smallest = index
        left = 2*index + 1
        right = 2*index + 2
        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left
        elif right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right
        if smallest != index:
            # why position swap ?
            self.pos[self.array[smallest][0]] = index
            self.pos[self.array[index][0]] = smallest
            self.swap_min_heap_node(smallest, index)
            self.min_heapify(smallest)

    def extract_min(self):
        if self.is_empty():
            return
        root = self.array[0]
        last_node = self.array[self.size - 1]
        self.pos[last_node[0]] = 0
        self.pos[root[0]] = self.size - 1
        self.size -= 1
        self.min_heapify(0)
        return root

    def is_empty(self):
        return True if self.size is 0 else False
