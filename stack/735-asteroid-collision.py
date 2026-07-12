from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0 and a < 0:
                    if stack[-1] < abs(a):
                        stack.pop()
                        continue
                    elif stack[-1] == abs(a):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(a)
        return stack
