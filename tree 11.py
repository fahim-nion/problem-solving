class BTNode:
    def __init__(self,elem):
        self.elem = elem
        self.left = left
        self.right = right
        
def inorder(root):
    if root == None:
        return

    inorder(root.left)
    print(root.elem, end = ' ')
    inorder(root.right)
    
def tree_construction(arr, i = 1):
    if i>=len(arr) or arr[i] == None:
        return None
    p = BTNode(arr[i])
    p.left = tree_construction(arr, 2*i)
    p.right = tree_construction(arr, 2*i+1)
    return p


def subtreeDiff(root,sum = 0):
    if root == None:
        return 0
    l_sum = 0
    if root.elem % 2 != 0:
        alice = l_sum + root.elem + subtreeDiff(root.left,l_sum)
    r_sum = 0
    if root.elem%2 == 0:
        bob = r_sum + root.elem + subtreeDiff(root.right,r_sum)
    if (alice - bob) < 1:
        return (alice-bob)*-1
    return (alice-bob)



class Node:
    def __init__(self, elem, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right

# Helper to sum odd numbers
def sum_odd(node):
    if node is None:
        return 0
    if node.elem % 2 != 0:
        return node.elem + sum_odd(node.left) + sum_odd(node.right)
    return sum_odd(node.left) + sum_odd(node.right)

# Helper to sum even numbers
def sum_even(node):
    if node is None:
        return 0
    if node.elem % 2 == 0:
        return node.elem + sum_even(node.left) + sum_even(node.right)
    return sum_even(node.left) + sum_even(node.right)

# Main function
def subtree_difference(root):
    if root is None:
        return 0
    
    alice_sum = sum_odd(root.left)
    bob_sum = sum_even(root.right)
    
    # Manually calculate absolute difference
    if alice_sum >= bob_sum:
        return alice_sum - bob_sum
    else:
        return bob_sum - alice_sum
