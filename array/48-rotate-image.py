class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we need to transpose first
        # and then reverse
        n = len(matrix)
        # transpose
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = (
                    matrix[col][row],
                    matrix[row][col],
                )
        # reverse, two pointer
        for row in range(n):
            left = 0
            right = n - 1
            while left < right:
                matrix[row][left], matrix[row][right] = (
                    matrix[row][right],
                    matrix[row][left],
                )
                left += 1
                right -= 1

        # Time: O(n^2)
        # Space: O(1)
