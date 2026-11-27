# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root

        while ancestor:
            if p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            elif p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            # If p and q vals are on opposite sides or they're equal to each other
            else:
                return ancestor