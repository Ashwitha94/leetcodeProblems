from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            stack = [node]
            visited[node] = True
            vertices = []
            degree_sum = 0

            while stack:
                u = stack.pop()
                vertices.append(u)
                degree_sum += len(graph[u])

                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)

            return len(vertices), degree_sum // 2

        for i in range(n):
            if not visited[i]:
                nodes, edges_count = dfs(i)
                if edges_count == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans