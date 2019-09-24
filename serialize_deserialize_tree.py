"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.
"""

class Node:
    def __init__ (self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

result = []

def preoder_recursive(node):
    if node:
        result.append(node.val)
        preoder_recursive(node.left)
        preoder_recursive(node.right)
    else:
        result.append('X')
    
    return result
        
def serialize(node):
    res = preoder_recursive(node)
    return '#'.join(res)

def deserialize(s):
    nodes = s.split('#')
    tree = restore_tree(nodes)

    return tree
    
def restore_tree(nodes):
    node = Node(None)

    if len(nodes) != 0:
        val = nodes.pop(0)
        if val != 'X':
            node = Node(val)
            node.left = restore_tree(nodes)
            node.right = restore_tree(nodes)

    return node 

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'