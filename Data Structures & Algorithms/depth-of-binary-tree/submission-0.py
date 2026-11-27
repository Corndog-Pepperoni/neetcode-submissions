# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Initialize stack with each element storing the node and it's depth in the tree
        stack = [(root, 1)]

        # Result represents the max depth
        res = 0

        # While there is a stack
        while stack:
            # Remove the last element (last in, first out)
            node, depth = stack.pop()

            # If the element popped is a node
            if node:
                # Determine the new result by comparing the current val of result with the
                # depth of the node in the tree
                res = max(res, depth)

                # Add the node's children to the stack
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        
        return res