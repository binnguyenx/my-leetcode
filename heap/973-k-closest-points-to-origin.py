import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # create heap to track
        max_heap = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            distance = x**2 + y**2
            heapq.heappush(max_heap, (-distance, i))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        res = []
        for dist, i in max_heap:
            res.append(points[i])
        return res

        # Time: O(n log k)
        # Space: O(k)
