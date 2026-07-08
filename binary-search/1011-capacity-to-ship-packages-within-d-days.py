from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            m = l + (r - l) // 2
            curr = 0
            day_need = 1
            for w in weights:
                if curr + w > m:
                    day_need += 1
                    curr = w
                    if day_need > days:
                        break
                else:
                    curr += w
            if day_need <= days:
                r = m
            else:
                l = m + 1
        return l
