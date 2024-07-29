# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0
        q = deque([root])
        
        while q:
            curlevel = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                curlevel.append(node.val)
            
            # Count the minimum swaps needed to sort curlevel
            sorted_level = sorted(curlevel)
            index_map = {v: i for i, v in enumerate(sorted_level)}
            
            visited = [False] * len(curlevel)
            
            for i in range(len(curlevel)):
                if visited[i] or index_map[curlevel[i]] == i:
                    continue
                
                cycle_size = 0
                x = i
                while not visited[x]:
                    visited[x] = True
                    x = index_map[curlevel[x]]
                    cycle_size += 1
                
                if cycle_size > 0:
                    res += cycle_size - 1

        return res
            
            