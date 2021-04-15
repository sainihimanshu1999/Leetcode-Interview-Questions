def LCA(self,root,p,q):
    if root in (None,p,q): return root
    left,right = (self.LCA(kid,p,q)
                    for kid in (root.left,root.right))
    return root if left and right else left or right