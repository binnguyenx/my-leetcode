from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # idea is sorting through the array, so just need to compare the first one and the last one
        # edge case: when the array is empty
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]
