# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


class Node:
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node: Node):
    val = node.val
    left = serialize(node.left) if node.left else None
    right = serialize(node.right) if node.right else None

    return [val, left, right]


def deserialize(node: list):
    val = node[0]
    left = deserialize(node[1]) if node[1] else None
    right = deserialize(node[2]) if node[2] else None

    return Node(val, left, right)


node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
print(deserialize(serialize(node)))
assert deserialize(serialize(node)).left.left.val == 'left.left'

