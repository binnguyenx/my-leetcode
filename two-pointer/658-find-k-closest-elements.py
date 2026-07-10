from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l + 1 > k:
            dis_l = abs(arr[l] - x)
            dis_r = abs(arr[r] - x)
            if dis_r < dis_l:
                l += 1
            else:
                r -= 1
        return arr[l:r + 1]
