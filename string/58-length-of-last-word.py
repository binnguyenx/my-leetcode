class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        count = 0
        # when first meet the space - count == 0 -> continue
        for i in range(n - 1, -1, -1):
            if s[i] != " ":
                count += 1
            elif count == 0 and s[i] == " ":
                continue
            elif count > 0:
                return count
        # if not meeting the space
        return count

        # Time: O(n)
        # Space: O(1)
