# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # time complexity: O(h) or O(logn) if it's a balanced tree
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            lmax = dfs(root.left)
            rmax = dfs(root.right)
            lmax = max(0, lmax)
            rmax = max(0, rmax)
            # The first line checks if the current node's full path (both       children included) is the best path.
            # The second line decides which one path (either left or right) should continue to the node's parent.
            res[0] = max(res[0], root.val + lmax + rmax)
            return root.val + max(lmax,rmax)
        
        dfs(root)
        return res[0]
