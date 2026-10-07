class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # 1,3,4,2
        # [1] -> [3] -> [4] -> [4,2] -> return -1
        # number in stack: cant find the next greater element -> return
        # map to store
        # if the next num larger - append to stack + hashmap
        stack = []
        next_greater = {}
        # build map
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)
        # take the num in stack
        while stack:
            num = stack.pop()
            next_greater[num] = -1
        res = []
        for num in nums1:
            res.append(next_greater[num])
        return res

        # Time: O(n)
        # Space: O(n)
