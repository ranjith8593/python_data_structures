class Heap:
    def __init__(self, v):
        self.items = []
        self.size = v

    def peek(self):
        if self.size == 0:
            return
        return self.items[0]
