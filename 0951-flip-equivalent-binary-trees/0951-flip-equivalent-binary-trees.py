# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        # Time Compelxity: 
        if not r1 or not r2:
            return not r1 and not r2 
        
        if r1.val != r2.val:
            return False
        
        a = self.flipEquiv(r1.left, r2.left) and self.flipEquiv(r1.right, r2.right) 
        # basically we have to find if it is possible to make r1 and r2 equal by either performing a flip or not performing a flip
        return a or self.flipEquiv(r1.left, r2.right) and self.flipEquiv(r1.right, r2.left)
