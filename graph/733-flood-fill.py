from collections import deque


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        starting_point = image[sr][sc]

        # If the starting color is unchanged, no traversal is needed
        if starting_point == color:
            return image

        rows = len(image)
        cols = len(image[0])

        # Use BFS to track the flood
        queue = deque([(sr, sc)])
        image[sr][sc] = color
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and image[new_row][new_col] == starting_point
                ):
                    image[new_row][new_col] = color
                    queue.append((new_row, new_col))

        return image

        # Time: O(m * n)
        # Space: O(m * n)
