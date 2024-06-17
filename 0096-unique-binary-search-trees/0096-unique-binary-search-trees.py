class Solution:
    def numTrees(self, n: int) -> int:
        # Time Complexity: O(n^2)
        # numTree[4] = numTree[0] * numTree[3] +
        #              numTree[1] * numTree[2] +
        #              numTree[2] * numTree[1] + 
        #              numTree[3] * numTree[1]
        # Dynamic Programming
        # n + 1 because we are starting from 0 to n
        numTrees = [1] * (n+1)
        # 0 nodes 1 tree
        # 1 nodes 1 tree
        for nodes in range(2, n+1):
            total = 0 
            for root in range(1, nodes+1):
                left = root - 1
                right = nodes - root 
                total += numTrees[left] * numTrees[right]
            numTrees[nodes] = total
        return numTrees[n]
