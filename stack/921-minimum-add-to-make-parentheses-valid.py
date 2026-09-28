class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # valid - empty string -> maybe no edge case
        # just use the count to store - open_count and add
        # open_count is the variable to store how many ( need to close
        # add is the open we need to add because we meet the close
        open_count = 0
        add = 0
        for char in s:
            # meet the open
            if char == "(":
                open_count += 1
            # meet the close
            else:
                # 2 situations - no more open count - lack of open to close
                if open_count > 0:
                    open_count -= 1
                else:
                    add += 1
        return add + open_count

        # Time: O(n)
        # Space: O(1)
