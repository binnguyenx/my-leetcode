from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # bfs + mark
        islands = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(start_r, start_c):
            queue = deque([(start_r, start_c)])
            # mark, if traverse -> mark grid[r][c] = "0"
            grid[start_r][start_c] = "0"
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    # condition is grid[nr][nc] == "1"
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == "1"
                    ):
                        # mark
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)

        return islands

        # Time: O(r * c)
        # Space: O(r * c)
