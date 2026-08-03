from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for start, end in intervals[1:]:
            # compare last and first of next one, x2 <= y1, merge, and then take the (x1, y2)
            last_end = ans[-1][1]
            if start <= last_end:
                # merging
                ans[-1][1] = max(end, last_end)
            # if 2 of them dont have same intervals
            else:
                ans.append([start, end])
        return ans
