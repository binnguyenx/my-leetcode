class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numbers = set(nums)
        longest = 0
        for x in numbers:
            # check if previous number exists or not
            # only start at the first of the group
            if x - 1 not in numbers:
                # move current from x -> update length
                current = x
                length = 1
                while current + 1 in numbers:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest

        # Time: O(n)
        # Space: O(n)
