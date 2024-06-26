# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # parent value 
        parent_val = root.val 

        # Value of p 
        p_val = p.val 

        # Value of q 
        q_val = q.val 

        # If both p and q are greater than parent 
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right,p,q)
        # If both p and q are lesser than parent 
        elif p_val < parent_val and q_val< parent_val:
            return self.lowestCommonAncestor(root.left,p,q)
        # we have found the split point 
        else:
            return root 