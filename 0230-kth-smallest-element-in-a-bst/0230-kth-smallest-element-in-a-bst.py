# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Time Complexity: O(h)
        def inorder(node):
            nonlocal count, result 

            if node is None:
                return
            
            # traverse the left subtree
            inorder(node.left)

            count += 1
            if count == k:
                result = node.val 
                return 
            
            # traverse the right 
            inorder(node.right)

        count = 0
        result = None 
        inorder(root)

        return result
        
        