class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        seen = {}
        # store the last index into hashmap
        for i in range(len(s)):
            seen[s[i]] = i
        # store 2 variables start and end
        # looping through the string
        # checking the max end - if find the char have more end - store new end
        res = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, seen[s[i]])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res

        # Time: O(n)
        # Space: O(n)
