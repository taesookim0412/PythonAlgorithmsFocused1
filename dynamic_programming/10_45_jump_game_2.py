import collections
import sys
from typing import List

# greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        lastJumpAmount = 1
        maxJumpAmount = 1
        for i in range(len(nums)):
            maxJumpAmount = max(maxJumpAmount - 1, nums[i])
            lastJumpAmount -= 1
            if lastJumpAmount == 0 and i != len(nums) - 1:
                lastJumpAmount = maxJumpAmount
                jumps += 1
        return jumps


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


