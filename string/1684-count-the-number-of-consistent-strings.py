from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow_map = set(allowed)
        count = 0
        for word in words:
            for char in word:
                if char not in allow_map:
                    break
            else:
                count += 1
        return count

        # Time: O(n * 26)
        # Space: O(1)
