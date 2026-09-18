from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        # bfs + mark - when visited mark 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(start_r, start_c):
            queue = deque([(start_r, start_c)])
            # mark the starting point
            grid[start_r][start_c] = 0
            area = 0
            while queue:
                r, c = queue.popleft()
                # increment area
                area += 1
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    # condition to mark
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):
                        # mark
                        grid[nr][nc] = 0
                        queue.append((nr, nc))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    max_area = max(max_area, area)

        return max_area
