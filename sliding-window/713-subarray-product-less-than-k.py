class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # use 2 pointers same direction
        # if the product more than k -> move the left pointer
        # if smaller than k -> add the answer
        # should ask count += right - left + 1
        # bc when product of subarray smaller than k -> all scenarios append
        # base case:
        if k <= 1:
            return 0
        count = 0
        l = 0
        product = 1
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k:
                product //= nums[l]
                l += 1
            count += r - l + 1
        return count
