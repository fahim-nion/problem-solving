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
    inorder(root.left)
    print(root.elem,end=" ")
    inorder(root.right)

def tree_construction(arr, i = 1):
    if i>=len(arr) or arr[i] == None:
        return None
    p = BTNode(arr[i])
    p.left = tree_construction(arr, 2*i)
    p.right = tree_construction(arr, 2*i+1)
    return p

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




'''
Level Min: 
Given a binary tree, find the smallest value in each level.
Sample Input: [You can use a dictionary here]
			              4 
              			/  \     
           		       9    2
           		     /  \     \
         		   3    -5    7

Sample Output:   4 2 -5

Explanation: 
There are 3 levels in the tree 
Level 0: {4}, min= 4
Level 1: {2, 9}, min= 2
Level 2: {7, 3, -5}, min = -5

'''
def smallest_level(root):
    return helper(root)

def helper(root,lvl ={},key=0):
    if root == None:
        return lvl
    elif key not in lvl:
        lvl[key] = root.elem
    elif lvl[key] > root.elem:
        lvl[key] == root.elem
    lvl = helper(root.left,lvl,key+1)
    lvl = helper(root.right,lvl,key+1)
    return lvl





#DRIVER CODE
root = tree_construction([None, 4,9,2,3,-5,None,7])
print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  3 9 5 4 2 7
print()
print('Level Wise Smallest Value: ', end = ' ')
print(smallest_level(root)) #Level Wise Smallest Value:  {0: 4, 1: 2, 2: -5}
     