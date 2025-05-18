def calculate_energy(root,k):
    if root == None:
        return 1
    if root.elem > k:
        calculate_energy(root.left,k)
    elif root.elem < k:
        calculate_energy(root.right,k)
        
        
        
        
        
class Node:
    def __init__(self, elem, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right

def calculate_energy(root, destination):
    product = 1
    found = False

    def helper(node, target):
        nonlocal product, found
        if node is None:
            return
        product *= node.elem
        if node.elem == target:
            found = True
            return
        if node.elem > target:
            helper(node.left, target)
        else:
            helper(node.right, target)
        if not found:
            product //= node.elem

    helper(root, destination)
    if found:
        return product
    else:
        return "route does not exist"