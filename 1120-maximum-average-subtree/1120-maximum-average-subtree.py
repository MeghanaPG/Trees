# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        # Time Complexity: 
        # Post Order Traversal
        res = 0 
        def traverse(node):
            if not node:
                return 0, 0
            nonlocal res 
            l_total, l_nodes = traverse(node.left)
            r_total, r_nodes = traverse(node.right)
            curr_total = l_total + r_total + node.val
            curr_nodes = l_nodes + r_nodes + 1
            res = max(curr_total/curr_nodes, res)
            return curr_total, curr_nodes
        traverse(root)
        return res