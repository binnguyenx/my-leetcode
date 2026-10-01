from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def solve(start, curr):
            # base case
            if len(curr) == k:
                res.append(curr[:])
                return
            # recursive phase
            for j in range(start, n + 1):
                curr.append(j)
                solve(j + 1, curr)
                curr.pop()

        solve(1, [])
        return res

        # Time: O(k * C(n, k))
        # Space: O(k)
