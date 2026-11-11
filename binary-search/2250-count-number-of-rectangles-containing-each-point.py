class Solution:
    def countRectangles(
        self, rectangles: list[list[int]], points: list[list[int]]
    ) -> list[int]:
        # take into height to satisfy height >= y
        # binary search to satisfy length >= x
        rec_map = {}
        for x, y in rectangles:
            if y not in rec_map:
                rec_map[y] = []
            rec_map[y].append(x)
        res = []
        # sort and then binary search
        for lengths in rec_map.values():
            lengths.sort()
        for x, y in points:
            count = 0
            for height, lengths in rec_map.items():
                if height < y:
                    continue
                elif height >= y:
                    l = 0
                    r = len(lengths)
                    while l < r:
                        m = (l + r) // 2
                        if lengths[m] < x:
                            l = m + 1
                        else:
                            r = m
                    # satisfy rectangle is the lengths of the lengths minus left pointer
                    count += len(lengths) - l
            res.append(count)
        return res

        # Time: O(n log n + m * h * log n)
        # Space: O(n)
