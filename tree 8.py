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


#check if identical or not



def are_identical(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1.elem != root2.elem:
        return False
    return are_identical(root1.left,root2.left) and are_identical(root1.right,root2.right)
    

arr1 = [None, 10, 5, 15, 3, 7, None, None]
root1 = tree_construction(arr1)
print("Tree 1 (inorder): ", end="")
inorder(root1)
print("\n")

# Tree 2 Construction (Identical to Tree 1)
#       10
#      /  \
#     5    15
#    / \
#   3   7
arr2 = [None, 10, 5, 15, 3, 7, None, None]
root2 = tree_construction(arr2)
print("Tree 2 (inorder): ", end="")
inorder(root2)
print("\n")

# Tree 3 Construction (Different structure)
#       10
#      /  \
#     5    15
#    /
#   3
arr3 = [None, 10, 5, 15, 3, None, None, None]
root3 = tree_construction(arr3)
print("Tree 3 (inorder): ", end="")
inorder(root3)
print("\n")

# Tree 4 Construction (Different values)
#       10
#      /  \
#     5    20  <-- Different value here
#    / \
#   3   7
arr4 = [None, 10, 5, 20, 3, 7, None, None]
root4 = tree_construction(arr4)
print("Tree 4 (inorder): ", end="")
inorder(root4)
print("\n")

# Tree 5 Construction (Empty Tree)
arr5 = [None]
root5 = tree_construction(arr5)
print("Tree 5 (inorder): ", end="") # Should print nothing
inorder(root5)
print("(Empty Tree)\n")

# Tree 6 Construction (Another Empty Tree)
root6 = None
print("Tree 6 (inorder): ", end="") # Should print nothing
inorder(root6)
print("(Empty Tree)\n")


# --- Test Cases for are_identical ---
print("--- Checking for Identical Trees ---")

# Test Case 1: Tree 1 and Tree 2 (Should be identical)
print(f"Are Tree 1 and Tree 2 identical? {are_identical(root1, root2)}")

# Test Case 2: Tree 1 and Tree 3 (Should NOT be identical - different structure)
print(f"Are Tree 1 and Tree 3 identical? {are_identical(root1, root3)}")

# Test Case 3: Tree 1 and Tree 4 (Should NOT be identical - different values)
print(f"Are Tree 1 and Tree 4 identical? {are_identical(root1, root4)}")

# Test Case 4: Tree 1 and Tree 5 (root1 vs empty tree)
print(f"Are Tree 1 and Tree 5 identical? {are_identical(root1, root5)}")

# Test Case 5: Tree 5 and Tree 6 (two empty trees)
print(f"Are Tree 5 and Tree 6 identical? {are_identical(root5, root6)}")

# Test Case 6: Tree with one node and another tree with one different node
root_single_A = BTNode(100)
root_single_B = BTNode(200)
print(f"Are single node tree (100) and single node tree (200) identical? {are_identical(root_single_A, root_single_B)}")
print(f"Are single node tree (100) and single node tree (100) identical? {are_identical(root_single_A, BTNode(100))}")

# Test Case 7: More complex different structure
# Tree 7:
#     10
#    /
#   5
#  /
# 3
arr7 = [None, 10, 5, None, 3]
root7 = tree_construction(arr7)
print("\nTree 7 (inorder): ", end="")
inorder(root7)
print("\n")
print(f"Are Tree 1 and Tree 7 identical? {are_identical(root1, root7)}")

# Test Case 8: Tree with only right children
# Tree 8:
# 1
#  \
#   2
#    \
#     3
root8 = BTNode(1)
root8.right = BTNode(2)
root8.right.right = BTNode(3)
print("Tree 8 (inorder): ", end="")
inorder(root8)
print("\n")

# Tree 9 (Same as Tree 8)
root9 = BTNode(1)
root9.right = BTNode(2)
root9.right.right = BTNode(3)

print(f"Are Tree 8 and Tree 9 identical? {are_identical(root8, root9)}")
print(f"Are Tree 1 and Tree 8 identical? {are_identical(root1, root8)}")



#chcek if binary tree is balanced?

def height(root):
    if root == None:
        return 0
    

def isBalanced(root):
    if root == None:
        return True
    lh = height(root.left)
    



def isDupli(root):
    if root == None:
        return False
    if 
    l_elem = isDupli(root.left)
    