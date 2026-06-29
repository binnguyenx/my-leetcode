from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #idea is checking the dif in hash or not
        hash = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in hash:
                return [i, hash[dif]]
            else:
                hash[nums[i]] = i
        return []
