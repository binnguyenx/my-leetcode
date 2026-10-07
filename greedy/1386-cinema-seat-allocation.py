class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # 1 row maximum 2 families
        # assume all is empty
        res = 2 * n
        # (2,3,4,5): left
        # (4,5,6,7): middle
        # (6,7,8,9): right
        # if left + middle + right free -> +2
        # if left or middle or right free -> +1
        # else: +0
        # map: key: row, value: cols
        seen = {}
        for i in range(len(reservedSeats)):
            row = reservedSeats[i][0]
            col = reservedSeats[i][1]
            if row not in seen:
                seen[row] = []
            seen[row].append(col)
        for row in seen:
            # left, right, middle
            left = True
            right = True
            middle = True
            cols = seen[row]
            # check for reserved
            for col in cols:
                if col in [2, 3, 4, 5]:
                    left = False
                if col in [4, 5, 6, 7]:
                    middle = False
                if col in [6, 7, 8, 9]:
                    right = False
            if left and middle and right:
                pass
            elif left or middle or right:
                res -= 1
            else:
                res -= 2
        return res

        # Time: O(n)
        # Space: O(n)
