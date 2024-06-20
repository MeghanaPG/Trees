# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Time Complexity:
        if not root:
            return None
    
        q = deque([(root, 0)])  # queue stores tuples of (node, level)
        prevLevel = -1
        leftmost_last_level_node = None

        while q:
            node, level = q.popleft()

            if level > prevLevel:
                # When we reach a new level, update our tracking variables
                prevLevel = level
                leftmost_last_level_node = node

            # Add child nodes to the queue if they exist
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        # After the loop, leftmost_last_level_node is the leftmost node at the last level
        return leftmost_last_level_node.val if leftmost_last_level_node else None