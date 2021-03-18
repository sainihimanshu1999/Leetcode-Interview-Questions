# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check_bst(root,float('-inf'),float('inf'))
    
    def check_bst(self,node,left,right):
        if not node:
            return True
        
        if not left<node.val<right:
            return False
        
        return(self.check_bst(node.left,left,node.val) and self.check_bst(node.right,node.val,right))
        
        