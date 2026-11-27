# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.matches(root, subRoot):
            return True
        
        # Return whether one of the sides contains the subroot
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def matches(self, root, subroot):
        # matches calls itself directly on the children of the current call of ifSubtree, so
        # we still need to check for None vals
        if not root and not subroot:
            return True
        if root and subroot and root.val == subroot.val:
            return self.matches(root.left, subroot.left) and self.matches(root.right, subroot.right)
        # When one of the trees do not exist or when their values don't match
        return False
        