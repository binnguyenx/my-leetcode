from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # delete nums[i-1] when nums[i-2] < num[i] -> we dont need to do anything because the loop turning
        # delete nums[i] when nums[i-2] > nums[i] -> nums[i] = nums[i-1]
        count = 0
        for i in range(1, len(nums)):
            # see the wrong one
            if nums[i - 1] >= nums[i]:
                count += 1
                if count > 1:
                    return False
                # logic deletion
                if i > 1 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
                else:
                    pass
        return True
