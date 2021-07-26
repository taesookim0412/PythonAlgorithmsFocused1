import collections
import sys
from typing import List

# brute force
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumpMap = collections.defaultdict(lambda: sys.maxsize)
        jumpMap[0] = 0
        for i, num in enumerate(nums):
            for amount in range(1, num + 1):
                newIndex = i + amount
                jumpMap[newIndex] = min(jumpMap[newIndex], jumpMap[i] + 1)
        return jumpMap[len(nums) - 1]


