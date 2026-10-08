class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            # if the character is different - skip left or right
            # and then check if it is a palindrome
            else:
                skip_l = s[l + 1 : r + 1]
                skip_r = s[l:r]
                return (skip_l == skip_l[::-1]) or (skip_r == skip_r[::-1])
        return True
