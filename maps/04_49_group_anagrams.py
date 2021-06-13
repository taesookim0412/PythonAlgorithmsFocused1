import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for i, s in enumerate(strs):
            sorted_s = ''.join(sorted(s))
            res[sorted_s] = res[sorted_s] + [s]
        return res.values()

print(
    Solution.groupAnagrams('',
    ["eat","tea","tan","ate","nat","bat"]
    )
)