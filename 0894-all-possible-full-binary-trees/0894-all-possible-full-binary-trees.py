# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        #Time complexity: 2^n
        dp = {0:[], 1: [TreeNode()]} #map n: list of FBT 
        #returns full binary tree with n nodes
        def backtrack(n):
            if n in dp:
                return dp[n]
            
            res = []
            for l in range(n): #0 to n-1 (Because we will be having one root node already)
                r = n - 1 - l
                leftTrees, rightTrees = backtrack(l), backtrack(r)
                
                #Basically we need possible trees of LeftTrees and rightTrees 
                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1,t2))
            dp[n] = res 
            return res 
        return backtrack(n)
                