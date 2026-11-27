# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(root):
            # dfs here cannot access the diameter in the global frame so make diamater
            # nonlocal to access it here
            nonlocal diameter
            if not root:
                # -1 because each recursive call automatically assumes the child exists with
                # the +1
                return -1

            # Get the max depths of the children
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)

            # Recalculate the diameter
            diameter = max(diameter, left + right)

            # Each child may have children, so return the max distance between the child's
            # children
            return max(left, right)
        
        dfs(root)
        return diameter

        
        