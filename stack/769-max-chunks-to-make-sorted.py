from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for cur in arr:
            if stack and cur < stack[-1]:
                highest_value = stack[-1]
                while stack and cur < stack[-1]:
                    stack.pop()
                stack.append(highest_value)
            else:
                stack.append(cur)
        return len(stack)
