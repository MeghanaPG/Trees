# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(h) or O(logn) if it's a balanced tree 
        res = [root.val]

        # We can have a max of 1 split to compute the res
        # return the max path without the split 
        def dfs(root):
            if not root:
                return 0 
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute the max path WITH the split 
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]