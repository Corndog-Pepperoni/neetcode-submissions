# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if there's no root, return None
        if not root:
            return None
        
        # Create a queue with the root
        queue = deque([root])
        while queue:
            # Pop the leftmost element in the queue and store it in node to process it (last
            # in first out)
            node = queue.popleft()

            # Swap the node's children
            node.left, node.right = node.right, node.left

            # If the node has children, append them to the queue to be processed in the next
            # loop
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root