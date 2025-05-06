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


root2 = tree_construction([None, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', None, None, None, 'I', 'J', None, 'k'])
inorder(root2)






def smallest_level(root, level = {}, key = 0):
    if root == None:
        return
    elif key not in level:
        level[key]=root.elem
    elif level[key] > root.elem:
        level[key] = root.elem
    lvl = smallest_level(root.left,level,key+1)
    lvl = smallest_level(root.right,level,key+1)
    return lvl


#DRIVER CODE
root = tree_construction([None, 4,9,2,3,-5,None,7])
print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  3 9 5 4 2 7
print()
print('Level Wise Smallest Value: ', end = ' ')
print(smallest_level(root)) #Level Wise Smallest Value:  {0: 4, 1: 2, 2: -5}