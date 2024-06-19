# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # Time Complexity: O(n)
        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                q.append(node.left)
                q.append(node.right)
            else:
                # here we expect everything to be null
                while q:
                    if q.popleft():
                        return False
        return True 

