class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        # base case
        if n == 1:
            return nums[0]

        def helper(arr):
            m = len(arr)
            if m == 1:
                return arr[0]
            dp = [0] * m
            dp[0] = arr[0]
            # take or skip
            # dp 2 times, first time skip the first index, second time skip last index
            dp[1] = max(arr[0], arr[1])
            for i in range(2, m):
                skip = dp[i - 1]
                take = dp[i - 2] + arr[i]
                dp[i] = max(skip, take)
            return dp[m - 1]

        # skip first house
        first_house = helper(nums[1:])
        # skip last house
        last_house = helper(nums[:-1])
        return max(first_house, last_house)

        # Time: O(n)
        # Space: O(n)
