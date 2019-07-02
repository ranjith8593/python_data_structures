class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def isBst(self, root, mini, max):
        if root is None:
            return True
        if root.data < mini or root.data > max:
            return False
        else:
            if self.isBst(root.left, mini, root.data) and self.isBst(root.right, root.data, max):
                return True
            else:
                return False


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    print(root.isBst(root, float("-inf"), float("inf")))