from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            # convert it to tuple to make it immutable to store in hashmap
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        # need to return the list of value
        return list(anagram_map.values())
