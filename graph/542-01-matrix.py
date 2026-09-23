from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # bfs + visited + multisource bfs
        rows = len(mat)
        cols = len(mat[0])
        # put all the 0 into the queue
        # bfs from that
        # if not 0, mark as -1
        queue = deque()
        distance = [[-1] * cols for _ in range(rows)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    distance[row][col] = 0
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr = dr + row
                nc = dc + col
                # conditions: meet unvisited cell -> distance of that cell + 1
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and distance[nr][nc] == -1
                ):
                    distance[nr][nc] = distance[row][col] + 1
                    queue.append((nr, nc))
        return distance
