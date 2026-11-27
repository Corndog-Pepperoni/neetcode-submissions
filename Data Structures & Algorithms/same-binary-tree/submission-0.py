# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Initialize queue pairing the parts of p with q
        queue = deque([(p, q)])

        # While there are still levels
        while queue:
            # For every element in the current level of both trees
            for _ in range(len(queue)):
                # Assign the current p node and q node
                p_node, q_node = queue.popleft()

                # Skip the rest of the code if the current nodes do not exist
                if p_node is None and q_node is None:
                    continue
                # If one of them don't exist or their values don't match
                if p_node is None or q_node is None or p_node.val != q_node.val:
                    return False
                
                # Append both tree's children to the queue for the next level
                queue.append((p_node.left, q_node.left))
                queue.append((p_node.right, q_node.right))

        return True
        