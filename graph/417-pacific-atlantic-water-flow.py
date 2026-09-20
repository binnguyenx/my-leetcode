from collections import deque


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # bfs from outside
        # so the lower -> higher
        # use just 1 variable start because we go through a list of coordinates
        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        # [r][c] is closer to the ocean
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        # add to ans + append to queue
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        # looping from the pacific ocean and atlantic ocean
        # find the starts
        pacific_starts = (
            [(0, c) for c in range(cols)]
            + [(r, 0) for r in range(rows)]
        )
        atlantic_starts = (
            [(rows - 1, c) for c in range(cols)]
            + [(r, cols - 1) for r in range(rows)]
        )

        # set for the pacific and atlantic
        # return the cells that exist in both
        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)
        return [[r, c] for r, c in pacific & atlantic]

        # Time: O(r * c)
        # Space: O(r * c)
