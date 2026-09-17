from collections import deque
from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        # build the graph first
        # bi-directional -> undirected
        # use bfs + visited
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([source])
        # mark as visited
        visited = {source}

        while queue:
            node = queue.popleft()
            # condition to return True
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False

        # Time: O(v + e)
        # Space: O(v + e)
