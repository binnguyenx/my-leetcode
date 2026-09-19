from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i == 0 or nums[i - 1] != nums[i]:
                l = i + 1
                r = n - 1
                while l < r:
                    sum_three = nums[i] + nums[l] + nums[r]
                    if sum_three == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif sum_three < 0:
                        l += 1
                    else:
                        r -= 1
        return res

        # Time: O(n^2)
        # Space: O(n)
