class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def level_order(self, root):
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.level_order(root)
