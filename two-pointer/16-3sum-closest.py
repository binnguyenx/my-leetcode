from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        # after i, we need 2 spaces for l and r
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == target:
                    return curr_sum
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                if curr_sum > target:
                    r -= 1
                else:
                    l += 1
        return closest_sum
