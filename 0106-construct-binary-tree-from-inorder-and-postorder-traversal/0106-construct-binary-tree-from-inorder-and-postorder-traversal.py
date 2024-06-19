# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Time Complexity: 
        inorderIdx = { v:i for i,v in enumerate(inorder)}

        def helper(l,r):
            if l > r:
                return None 

            root = TreeNode(postorder.pop())

            mid = inorderIdx[root.val]
            root.right = helper(mid+1, r)
            root.left = helper(l, mid-1)
           
            return root

        return helper(0, len(inorder)-1) 