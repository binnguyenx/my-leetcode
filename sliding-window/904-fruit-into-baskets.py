from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # hash map + sliding window
        count = defaultdict(int)
        l = 0
        longest = 0
        for r in range(len(fruits)):
            # put the fruits[r] into the map
            count[fruits[r]] += 1
            # looping to delete the left if not satisfy the condition
            while len(count) > 2:
                # delete the left first
                count[fruits[l]] -= 1
                # if the left == 0 -> delete the key
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                # move the left
                l += 1
            # update the answer
            longest = max(longest, r - l + 1)
        return longest
