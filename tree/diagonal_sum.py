class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.dia = None

    def print_diagonal(self, root, diagonal):
        if root is None:
            return
        if root.left:
            diagonal_val = root.dia + 1
            root.left.dia = diagonal_val
            if diagonal_val in diagonal:
                diagonal[diagonal_val].append(root.left.data)
            else:
                diagonal[diagonal_val] = [root.left.data]
            self.print_diagonal(root.left, diagonal)
        if root.right:
            root.right.dia = root.dia
            if root.dia in diagonal:
                diagonal[root.dia].append(root.right.data)
            else:
                diagonal[root.dia] = [root.right.data]
            self.print_diagonal(root.left, diagonal)
        return diagonal


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(9)
    root.left.right = Node(6)
    root.right.left = Node(4)
    root.right.right = Node(5)
    root.right.left.right = Node(7)
    root.right.left.left = Node(12)
    root.left.right.left = Node(11)
    root.left.left.right = Node(10)
    root.dia = 0
    diagonal = {0:[root.data]}
    print(root.print_diagonal(root, diagonal))

