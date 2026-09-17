from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        # bfs + visited set
        # set stores the rooms that we have visited
        queue = deque([0])
        visited = {0}

        while queue:
            room = queue.popleft()
            # looping through the keys of the room
            for key in rooms[room]:
                # condition to check if it is in the set or not
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        # return when length of the set == length of the rooms
        return len(visited) == n

        # Time: O(v + e)
        # Space: O(v)
