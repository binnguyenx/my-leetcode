from collections import Counter
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            # checking the size of heap
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # O(log k)
        # taking out the num
        res = []
        for freq, num in min_heap:
            res.append(num)
        return res
