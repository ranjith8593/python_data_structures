class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def path_sum(self, root, sum_v, path):
        if root is None and sum_v is 0:
            print(path)
        elif root is None and sum_v is not 0:
            return
        else:
            remaining = sum_v - root.data
            path.append(root.data)
            self.path_sum(root.left, remaining, path)
            self.path_sum(root.right, remaining, path)


if __name__ == "__main__":
    s = 21
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.right = Node(5)
    root.left.left = Node(3)
    root.right.left = Node(2)
    root.path_sum(root, s, [])
