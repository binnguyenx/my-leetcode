from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0 space: left to low - 1
        # 1 space: low to mid - 1
        # none space: mid to high
        # 2 space: high + 1 to end
        low = 0
        mid = 0
        high = len(nums) - 1
        # if mid = 0, swap low and mid, increment low and mid
        # if mid = 1, increment mid
        # if mid = 2, swap mid and high
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
