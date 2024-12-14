'''
Convert A Binary tree to its mirror

            10           10
            /\           /\
           20 30        30 20
          /  \            /  \
         40  60          60  40



'''
class BTNode:
    def __init__(self,elem):
        self.elem = elem
        self.left = None
        self.right = None

def inorder(root):
    if root == None:
        return 
    

def convert_mirror(root):
    if root == None:
        return None
    node = BTNode(root.elem)
    node.left = convert_mirror(root.right)
    node.right = convert_mirror(root.left)
    return node





#DRIVER CODE
root = BTNode(10)
n1 = BTNode(20)
n2 = BTNode(30)
n3 = BTNode(40)
n4 = BTNode(60)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  40 20 60 10 30
print()

root2 = convert_mirror(root)
print('Mirrored Tree Inorder Traversal: ', end = ' ')
inorder(root2) #Mirrored Tree Inorder Traversal:  30 10 60 20 40