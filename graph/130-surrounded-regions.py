from collections import deque


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # find O surrounded by X -> turn to X
        # find O not surrounded by X
        # so we find the border O -> mark with S
        # the O inside -> mark with X
        def bfs(start_r, start_c):
            # mark the starting point
            board[start_r][start_c] = "S"
            queue = deque([(start_r, start_c)])
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    # condition to mark
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and board[nr][nc] == "O"
                    ):
                        board[nr][nc] = "S"
                        queue.append((nr, nc))

        # left and right borders
        for r in range(rows):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][cols - 1] == "O":
                bfs(r, cols - 1)

        # upper and lower borders
        for c in range(cols):
            if board[0][c] == "O":
                bfs(0, c)
            if board[rows - 1][c] == "O":
                bfs(rows - 1, c)

        # marking O -> X and S -> O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
