class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        l = 0
        max_len = 0
        for r in range(n):
            # checking if in set
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            # if not in set
            seen.add(s[r])
            length = r - l + 1
            max_len = max(max_len, length)
        return max_len
