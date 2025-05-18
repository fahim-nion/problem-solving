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
  
def tree_construction(arr, i = 1):
    if i>=len(arr) or arr[i] == None:
        return None
    p = BTNode(arr[i])
    p.left = tree_construction(arr, 2*i)
    p.right = tree_construction(arr, 2*i+1)
    return p

#mid practice

#counting nodes of the tree 

def count(root):
    if root == None:
        return 0
    else:
        1 + count(root.left) + count(root.right)
        
#finding level of a Node
def get_lvl(root,elem,root_lvl):
    if root == None:
        return 0
    if root.elem == elem:
        return root_lvl
    down_lvl = get_lvl(root.left,elem,root_lvl +1)  #0
    if down_lvl != 0:
        return down_lvl
    down_lvl = get_lvl(root.right,elem,root_lvl+1)
    return down_lvl