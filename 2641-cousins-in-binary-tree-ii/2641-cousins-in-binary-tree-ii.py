# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.val = 0
        else:
            return None
        que = deque()
        que.append(root)
        path_total = defaultdict(int)
        while que:
            node_arr = []
            total_sum = 0
            for _ in range(len(que)):

                node = que.popleft()
                node_arr.append(node)

                if node.left:
                    que.append(node.left)
                    path_total[node]+=node.left.val
                    total_sum+=node.left.val
                
                if node.right:
                    que.append(node.right)
                    path_total[node]+=node.right.val
                    total_sum+=node.right.val
                
            for node in node_arr:
                # sum of all children values at the current level minus the sum of the node's children's values.
                # For node 4:
                # Left child (1): 1.val = total_sum - path_total[4] = 18 - 11 = 7.
                # Right child (10): 10.val = total_sum - path_total[4] = 18 - 11 = 7.
                if node.left:
                    node.left.val = total_sum - path_total[node]
                if node.right:
                    node.right.val = total_sum - path_total[node]
        return root
            

