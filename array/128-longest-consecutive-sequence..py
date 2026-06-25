class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)
        #idea is looping through the seen
        #find the first of the line
        #checking if the first is in the seen or not, if not, that will be the first
        for i in seen:
            if (i - 1) not in seen:
                length = 1
                #use while to find the maximum length
                while (i + length) in seen:
                    length += 1
                longest = max(length, longest)
        return longest