# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both do not exist (reached end of both trees)
        if p is None and q is None:
            return True
        # If only one end of a tree is met or if the current node vals don't match
        if p is None or q is None or p.val != q.val:
            return False

        # Return whether both sides of p match both sides of q
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)