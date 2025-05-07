class BTNode:
    def __init__(self, elem):
        self.elem = elem
        self.right = None
        self.left = None
    
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.elem, end = ' ')
    inorder(root.right)
    print()

def tree_construction(arr, i = 1):
    if i>=len(arr) or arr[i] == None:
        return None
    p = BTNode(arr[i])
    p.left = tree_construction(arr, 2*i)
    p.right = tree_construction(arr, 2*i+1)
    return p

def identical(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1.elem != root2.elem:
        return False
    return identical(root1.left,root2.left) and identical(root1.right,root2.right)
        

# Test Case 1: Identical trees
root1 = tree_construction([None, 1, 2, 3])
root2 = tree_construction([None, 1, 2, 3])
print("Test Case 1 - Trees are identical:", identical(root1, root2))  # Expected: True

# Test Case 2: Non-identical trees
root3 = tree_construction([None, 1, 3, 2])
print("Test Case 2 - Trees are identical:", identical(root1, root3))  # Expected: False

# Test Case 3: One empty tree
root4 = None
print("Test Case 3 - Trees are identical:", identical(root1, root4))  # Expected: False

# Test Case 4: Both empty trees
print("Test Case 4 - Trees are identical:", identical(root4, root4))  # Expected: True

# Test Case 5: Different structure
root5 = tree_construction([None, 1, 2, None, 3])
root6 = tree_construction([None, 1, 2, 3])
print("Test Case 5 - Trees are identical:", identical(root5, root6))  # Expected: False

# Additional test case from the example
root7 = tree_construction([None, 1, 2, 3])
root8 = tree_construction([None, 1, 3, 2])
print("Example Test Case - Trees are identical:", identical(root7, root8))  # Expected: False
root.left = 2
root.right = 3

