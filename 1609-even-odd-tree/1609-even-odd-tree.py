# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # Time Complexity: O(n)
        # Level order traversal - BFS

        even = True 
        q = deque([root])

        while q:
            prev = float("-inf") if even else float("inf")
          
            for i in range(len(q)):
                node = q.popleft()
                if even and (node.val % 2 == 0 or node.val <= prev):
                        return False
                elif not even and (node.val % 2 == 1 or node.val >= prev):
                        return False
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                prev = node.val 
            # we need to make sure we keep track of the level we are at
            even = not even
        return True 