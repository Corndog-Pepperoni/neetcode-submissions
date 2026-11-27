# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Initialize queue
        queue = deque()

        # Check if there is a given root input since deque only takes iterables
        if root:
            queue.append(root)

        # Initialize depth
        depth = 0

        # While there are still levels in the tree
        while queue:
            # Iterate through every item in the current level
            # Used range(len(queue)) instead of item in queue because because queue cannot be
            # mutated during iteration (we also only want to process the nodes already queued
            # for this level)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        
        return depth

