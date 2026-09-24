from collections import deque


class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        k = len(connections)
        # base case
        if k < n - 1:
            return -1
        # make a graph
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        components = 0
        # bfs + marking
        # the result will be the components - 1
        visited = [False] * n
        for start in range(n):
            # if we visit already -> continue
            # if not -> visited + mark
            if visited[start]:
                continue
            components += 1
            visited[start] = True
            queue = deque([start])
            while queue:
                curr = queue.popleft()
                # looping through the neighbor
                for neighbor in graph[curr]:
                    # if not visited -> mark -> append to queue
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
        return components - 1
