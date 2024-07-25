# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # dfs and constructing the BST 
        # in order traversal -> left - root - right 

        def inorder(root):
            stack = []
            res = []
            current = root 

            while current is not None or stack:
                while current is not None:
                    stack.append(current)
                    current = current.left 
                
                current = stack.pop()
                res.append(current.val)
                current = current.right 
        
            return res 

        def construct_tree(res):
            if not res:
                return None
            
            # mid of inorder traversal sorted list becomes the root 
            mid = len(res) // 2
            root = TreeNode(res[mid])
            root.left = construct_tree(res[:mid])
            root.right = construct_tree(res[mid+1:])
            return root 

        inorder_result = inorder(root)
        return construct_tree(inorder_result)


