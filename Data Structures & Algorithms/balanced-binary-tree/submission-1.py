# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Create balanced list which keeps track of whether every node in the tree is balanced
        balanced = []

        def dfs(root):
            if not root:
                return -1

            leftHeight = 1 + dfs(root.left)
            rightHeight = 1 + dfs(root.right)

            # add T or F to balanced depending on whether the left and right height difference
            # is <= 1
            balanced.append(abs(leftHeight - rightHeight) <= 1)

            # Return the max height of the subtree to the parent
            # This is used to compare the longest path from the left side with the right side
            return max(leftHeight, rightHeight)
        
        dfs(root)
        return all(balanced)
