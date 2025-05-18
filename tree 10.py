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


def wizard(root1,root2,k):
    if root1 == None and root2 == None:
        return
    if root1.elem == root2.elem:
        val = root1.elem 
    
    
    
    
    
    
    
def max_path_sum(root):
    def helper(root,sum = 0):
        if root == None:
            return 0
        sum += root.elem
        l_s = helper(root.left,sum)
        r_s = helper(root.right,sum)
        
        
        
        
def oddSwapp(root):
    def helper(root , lvl = 0):
        if root == None :
            return
        if lvl%2 ! = 0:
            if root.left != None and root.right != None:
                if root.left.elem < root.right.elem:
                    root.left,root.right = root.right,root.left
        helper(root.left, lvl +1)
        helper(root.right, lvl + 1)
    helper(root)
    return root