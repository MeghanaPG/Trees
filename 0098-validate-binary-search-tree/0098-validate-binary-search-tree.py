# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, l, r):
            if not node:
                return True 
            
            if not (node.val > l and node.val < r):
                return False 
            
            return isValid(node.left, l, node.val) and isValid(node.right, node.val, r)
        return isValid(root, float("-inf"), float("inf"))
        
        
        
        
        
