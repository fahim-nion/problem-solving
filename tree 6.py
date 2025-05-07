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
print()

def level_sum(root):
    def helper(root,level=0):
        if root == None:
            return 0
        else:
            if level % 2 == 0:
                val = (-root.elem)
            else:
                val = root.elem
        return val + helper(root.left,level + 1) + helper(root.right,level + 1)
    return helper(root)

#DRIVER CODE
root = BTNode(1)
n2 = BTNode(2)
n3 = BTNode(3)
n4 = BTNode(4)
n5 = BTNode(5)
n6 = BTNode(6)
n7 = BTNode(7)
n8 = BTNode(8)
root.left = n2
root.right = n3

n2.left = n4
n3.left = n5
n3.right = n6

n5.left = n7
n5.right = n8


print(level_sum(root)) #This should print 4