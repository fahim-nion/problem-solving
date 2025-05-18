class BTNode:
    def __init__(self,elem,left = None,right = None):
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



def left_energy_signature(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        
    left_energy_signature(root.left)