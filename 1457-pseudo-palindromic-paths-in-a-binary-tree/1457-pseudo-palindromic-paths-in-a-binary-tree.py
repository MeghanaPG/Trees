# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # Time complexity: O(n) / O(h)
        # using defaultdict is better to be used in many cases 
        # as it doesn't throw the key error 
        count = defaultdict(int)
        odd = 0 #digits with odd count 

        def dfs(curr):
            nonlocal odd
            if not curr:
                return 0 
            
            count[curr.val] += 1
            # in the path we are checking the number of odd vals
            odd_change = 1 if count[curr.val] % 2 == 1 else -1 
            # if we are traversing back the path, we will have to remove some changes
            odd += odd_change 

            if not curr.left and not curr.right:
                res = 1 if odd <= 1 else 0     
            else:
                res = dfs(curr.left) + dfs(curr.right)
            # resetting the value as we are doing the backtrack
            odd -= odd_change 
            count[curr.val] -= 1
            return res
            
        return dfs(root)
