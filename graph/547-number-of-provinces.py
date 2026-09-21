from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # bfs + visited
        # [i][j] is from city i to city j, if it == 1 -> 2 cities are connected
        # bfs through that -> mark connected if [i][j] == 1 and not visited
        visited = [False] * n
        provinces = 0

        # looping through each city
        for start in range(n):
            # if we visit that city already -> move on
            if visited[start]:
                continue
            provinces += 1
            visited[start] = True
            queue = deque([start])
            while queue:
                city = queue.popleft()
                # looping through cities connected with the current city
                for neighbor in range(n):
                    if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

        return provinces

        # Time: O(n^2)
        # Space: O(n)
