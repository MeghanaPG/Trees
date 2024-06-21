# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # Time Complexity: O(n)

        if not root:
            return root
        
        def helper(node):
            if not node:
                return None 
            
            node.left = helper(node.left)
            node.right = helper(node.right)

            # condition to check if it is leaf node
            if not node.left and not node.right and node.val == target:
                # returning None to delete that node
                return None 
            
            return node 
        
        # starting from the helper 
        return helper(root)