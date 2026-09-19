class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # without repeating -> set
        n = len(s)
        # creating window
        seen = set()
        res = 0
        l = 0
        for r in range(n):
            # if it in seen -> remove until the left not in
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max((r - l + 1), res)
        return res

        # Time: O(n)
        # Space: O(n)
