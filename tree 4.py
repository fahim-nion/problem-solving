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


def swap_child(root, level, M):
    if root == None:
        return
    if level != M:
        left = swap_child(root.left,level+1,M)
        right = swap_child(root.right,level+1,M)
        root.left = right
        root.right = left
    return root


#Driver Code
root=BTNode('A')
n1 = BTNode("B")
n2 = BTNode("C")
root.left = n1
root.right = n2
n3 = BTNode("D")
n4 = BTNode("E")
n1.left = n3
n1.right = n4
n5 = BTNode("G")
n6 = BTNode("H")
n3.left = n5
n3.right = n6
n7 = BTNode("I")
n4.left = n7
n4.left = None
n2.left = None
n8 = BTNode("F")
n2.right = n8
n9 = BTNode("J")
n8.left = n9
n8.right = None





print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root)   #Given Tree Inorder Traversal: G D H B I E A C J F
print()

root2 = swap_child(root, 0, 2)
print('Swapped Tree Inorder Traversal: ', end = ' ')
inorder(root2)  #Swapped Tree Inorder Traversal: J F C A I E B G D H