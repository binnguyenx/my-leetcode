from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # make it into a graph
        # if have cycle -> return []
        # if not -> return the order
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
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for nei in graph[node]:
                # update indegree
                indegree[nei] -= 1
                # append to queue
                if indegree[nei] == 0:
                    queue.append(nei)
        if len(res) == numCourses:
            return res
        return []

        # Time: O(v + e)
        # Space: O(v + e)
