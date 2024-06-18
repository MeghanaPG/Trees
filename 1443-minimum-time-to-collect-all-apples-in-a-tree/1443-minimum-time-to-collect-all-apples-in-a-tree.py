class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    # Time Complexity:O(n)
    # More of a Graph problem
    # mapping node to an empty arr initially
        adj = {i:[] for i in range(n)}

        for par, child in edges:
            adj[par].append(child)
            adj[child].append(par)

        def dfs(cur, par):
            time = 0 

            for child in adj[cur]:
                if child == par:
                    continue 
                childTime = dfs(child, cur)
                if childTime or hasApple[child]:
                    # 2 is because for going and traversing back
                    time += 2 + childTime
            return time 
        return dfs(0, -1)



