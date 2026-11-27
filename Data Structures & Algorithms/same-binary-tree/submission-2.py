# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Initialize stack for iterative DFS that stores the corresponding parts of p and q
        stack = [(p, q)]

        # While the trees can still be searched down
        while stack:
            # Assign p and q nodes (last in first out)
            p_node, q_node = stack.pop()

            # If both trees end
            if not p_node and not q_node:
                continue
            # If only one of the trees end or if their vals don't match
            if not p_node or not q_node or p_node.val != q_node.val:
                return False
            
            # Append their children to the stack
            stack.append((p_node.left, q_node.left))
            stack.append((p_node.right, q_node.right))
        
        return True