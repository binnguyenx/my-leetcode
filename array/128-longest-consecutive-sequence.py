class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # union find
        parent = {}
        size = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            # find two roots
            root_a = find(a)
            root_b = find(b)
            # edge case
            if root_a == root_b:
                return
            # root_a is the root of the bigger group
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            size[root_a] += size[root_b]

        longest = 0
        for x in nums:
            # if already in a group -> continue
            if x in parent:
                continue
            # create a group for that
            parent[x] = x
            size[x] = 1
            if x - 1 in parent:
                union(x, x - 1)
            if x + 1 in parent:
                union(x, x + 1)
            longest = max(longest, size[find(x)])
        return longest
