class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        # left, top, diag
        # dp[i] = min(top, left, diag) + 1
        res = 0
        for r in range(rows):
            for c in range(cols):
                # base case: first row/col - if matrix[r][c] == "1" -> dp = 1
                if matrix[r][c] == "1":
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = 1 + min(
                            dp[r - 1][c],
                            dp[r][c - 1],
                            dp[r - 1][c - 1],
                        )
                    res = max(res, dp[r][c])
        return res * res
