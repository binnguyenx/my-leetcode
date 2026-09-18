"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # use bfs to clone + hashing
        # base case: if none -> return None
        # first node into queue
        # for each neighbor:
        # if not clone -> clone and add to queue
        # link clone node with clone neighbor
        if not node:
            return None

        # create a hashmap with key:value is ori node: copy node
        copies = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            original = queue.popleft()
            # node is original
            clone = copies[original]
            for neighbor in original.neighbors:
                if neighbor not in copies:
                    copies[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # connect the clone node with the clone neighbors
                clone.neighbors.append(copies[neighbor])

        return copies[node]
