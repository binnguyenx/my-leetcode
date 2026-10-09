class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        rows = len(matrix)
        cols = len(matrix[0])
        # when to stop: top > bottom, left > right
        while top <= bottom and left <= right:
            # left to right
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1
            # top to bot
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1
            # right to left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1
            # bot to top
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1
        return res
