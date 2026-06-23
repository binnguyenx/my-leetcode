from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            res = []
            # two pointers for tracking the merge
            i = j = 0
            # need to go through all left or right, because maybe left > right or right > left
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            while i < len(left):
                res.append(left[i])
                i += 1
            while j < len(right):
                res.append(right[j])
                j += 1
            return res

        def merge_sort(arr):
            # base case
            if len(arr) <= 1:
                return arr
            # divide
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        return merge_sort(nums)
