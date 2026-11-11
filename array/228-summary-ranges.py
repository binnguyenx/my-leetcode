class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # base case
        if not nums:
            return []
        res = []
        start = nums[0]
        end = nums[0]
        for i in range(1, len(nums)):
            # if end is as same as the next nums - move end
            if nums[i] == end + 1:
                end = nums[i]
            else:
                # if not - close range
                if start == end:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{end}")
                start = nums[i]
                end = nums[i]
        # add the last one
        if start == end:
            res.append(str(start))
        else:
            res.append(f"{start}->{end}")
        return res

        # Time: O(n)
        # Space: O(1)
