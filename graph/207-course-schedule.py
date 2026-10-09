from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # make it into a graph
        # if have cycle -> return false
        # if not -> return True
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        # make a graph
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        queue = deque()
        # loop - if indegree == 0 -> put it into queue
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for nei in graph[node]:
                # update indegree
                indegree[nei] -= 1
                # append to queue
                if indegree[nei] == 0:
                    queue.append(nei)
        # check cycle
        return count == numCourses

        # Time: O(v + e)
        # Space: O(v + e)
