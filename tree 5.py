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


def subtract_summation(root):
    l_sum = sum(root.left)
    r_sum = sum(root.right)
    return l_sum - r_sum

def sum(root):
    if root == None:
        return 0
    return root.elem + sum(root.left) + sum(root.right)



#Driver Code
root=BTNode(71)
n1 = BTNode(27)
n2 = BTNode(62)
n3 = BTNode(80)
n4 = BTNode(75)
n5 = BTNode(41)
n6 = BTNode(3)
n7 = BTNode(87)
n8 = BTNode(56)
n9 = BTNode(19)
n10 = BTNode(89)


root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

n3.left = n7
n3.right = n8

n2.left = n5
n2.right = n6

n6.left = n9
n6.right = n10

print(subtract_summation(root)) #This should print 111