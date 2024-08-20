# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        # Time Complexity:
        t1 = set()
        found = False 

        def dfs(node):
            if node is None:
                return 

            dfs(node.left)
            t1.add(node.val)
            dfs(node.right)

        dfs(root1)

        def dfs2(node):
            if node is None:
                return 
            
            dfs2(node.left)
            if target - node.val in t1:
                nonlocal found
                found = True
            dfs2(node.right)
        
        dfs2(root2)
        return found 