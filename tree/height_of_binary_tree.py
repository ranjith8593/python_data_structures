class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def height_of_tree(self, root):
        if root is None:
            return 0
        height = max((self.height_of_tree(root.left) + 1),(self.height_of_tree(root.right) +1))
        return height


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(root.height_of_tree(root))
