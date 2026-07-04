from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]

        for u, v, d in roads:
            adj[u].append((v, d))
            adj[v].append((u, d))

        visited = [False] * (n + 1)
        ans = float('inf')

        def dfs(node):
            nonlocal ans
            visited[node] = True

            for nei, dist in adj[node]:
                ans = min(ans, dist)
                if not visited[nei]:
                    dfs(nei)

        dfs(1)
        return ans