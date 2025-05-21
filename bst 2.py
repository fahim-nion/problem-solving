def mirrorFree(root, e):
    if root == None:
        return
    if e < root.elem:
        l_t = mirrorFree(root.left,e) 