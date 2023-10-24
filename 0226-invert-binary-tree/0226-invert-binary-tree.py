# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time Complexity: O(n) -> n is the number of nodes 
        if not root:
            return None 
        else:
            # return the modified node 
            return self.swap_left_right(root) 

    # recursion 
    def swap_left_right(self, node):
        if node:
            temp = node.left
            node.left = node.right 
            node.right = temp 
        
            self.swap_left_right(node.left)
            self.swap_left_right(node.right)
        return node 