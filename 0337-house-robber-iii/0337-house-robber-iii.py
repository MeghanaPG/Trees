# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(n)
        # cases: [with root, without root]
        # DFS with some modifications

        # returns a pair of values for w root and w/o the root 
        def dfs(root):
            if not root:
                return [0,0]
            
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            #second value as we need the node after the root -> first -> second
            withRoot = root.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]
        return max(dfs(root))



