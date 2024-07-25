# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_diff = 0

        def helper(node, cur_max, cur_min):
            if not node:
                return None 
            # This ensures that the function captures the maximum absolute difference between the current node and any of its ancestors.
            self.max_diff = max(self.max_diff, abs(cur_max - node.val),
                                abs(cur_min - node.val))
    
            
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)

        helper(root, root.val, root.val)
        return self.max_diff