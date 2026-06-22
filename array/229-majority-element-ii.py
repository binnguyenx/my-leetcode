from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # edge case
        if not nums:
            return []
        # bayer moore alg - candidate 1, 2 - read write pointer
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            # num as same as cand1
            if num == cand1:
                count1 += 1
            # num as same as cand2
            elif num == cand2:
                count2 += 1
            # cand1 is empty
            elif count1 == 0:
                cand1 = num
                count1 = 1
            # cand2 is empty
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        # checking if it more than n / 3
        target = len(nums) / 3
        res = []
        actual_count_1 = nums.count(cand1) if cand1 is not None else 0
        actual_count_2 = nums.count(cand2) if cand2 is not None else 0
        if actual_count_1 > target:
            res.append(cand1)
        if actual_count_2 > target and cand1 != cand2:
            res.append(cand2)
        return res
