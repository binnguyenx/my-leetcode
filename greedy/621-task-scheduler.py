from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # A A A A
        # B B
        # C
        # D
        # n = 2
        # A _ _ A _ _ A _ _ A
        # A B C A B idle A D idle A
        # return 10
        # A - n slot - A -....
        # max freq A: 4
        # (max_freq - 1) * n + max_freq + number of tasks that have freq = maxFreq
        # A A A A A n = 2
        # A B _ A B _ A B
        count = Counter(tasks)
        max_freq = max(count.values())
        max_count = 0
        for freq in count.values():
            if freq == max_freq:
                max_count += 1
        res = (max_freq - 1) * n + max_freq - 1 + max_count
        return max(len(tasks), res)
