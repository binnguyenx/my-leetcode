from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        # create a graph
        graph = defaultdict(list)
        # 1: [2, 3]
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)

        start = None
        # find the first (endpoint with degree 1)
        for node in graph:
            if len(graph[node]) == 1:
                start = node
                break

        res = []
        stack = [(start, None)]
        while stack:
            curr, prev = stack.pop()
            res.append(curr)
            for neighbor in graph[curr]:
                # skip the one that we visited
                if neighbor != prev:
                    stack.append((neighbor, curr))
        return res

        # Time: O(n)
        # Space: O(n)
