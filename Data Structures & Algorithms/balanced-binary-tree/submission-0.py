# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = []

        def dfs(root):
            if not root:
                return -1

            leftHeight = 1 + dfs(root.left)
            rightHeight = 1 + dfs(root.right)

            balanced.append(abs(leftHeight - rightHeight) <= 1)

            return max(leftHeight, rightHeight)
        
        dfs(root)
        return all(balanced)
