# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        pathSum = 0 

        def dfs(node, pathSum):
            if not node:
                return False
            
            pathSum += node.val 
            # leaf node 
            if not node.left and not node.right:
                return pathSum >= limit 
            left = dfs(node.left,pathSum)
            right = dfs(node.right,pathSum)
            if not left:
                node.left = None 
            if not right:
                node.right = None 
            return left or right 
        res = dfs(root,0)
        return root if res else None 

