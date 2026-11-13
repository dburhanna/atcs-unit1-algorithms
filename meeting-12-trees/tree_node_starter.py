class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)

    elif value > root.value:
        root.right = insert(root.right, value)

    # Duplicate values are ignored.
    return root


def contains(root, target):
    if root is None:
        return False

    if target == root.value:
        return True

    if target < root.value:
        return contains(root.left, target)

    return contains(root.right, target)


root = None

values = [50, 25, 75, 10, 35, 60, 90]

for value in values:
    root = insert(root, value)

print(contains(root, 35))  # True
print(contains(root, 60))  # True
print(contains(root, 40))  # False
