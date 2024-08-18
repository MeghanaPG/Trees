# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # Time and Space: O(n), O(h)
        # Preorder Traversal: root -> left -> right
        def preorder(r, curr_number):
            nonlocal root_to_leaf
            if r:
                curr_number = (curr_number << 1) | r.val
                # we update the sum if it's a leaf
                if not (r.left or r.right):
                    root_to_leaf += curr_number
                
                preorder(r.left, curr_number)
                preorder(r.right, curr_number)
        
        root_to_leaf = 0
        preorder(root,0)
        return root_to_leaf