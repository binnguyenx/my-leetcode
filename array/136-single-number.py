class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # xor
        result = 0
        for num in nums:
            result ^= num
        return result
