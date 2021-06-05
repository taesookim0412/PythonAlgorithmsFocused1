from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        runningCt = 0
        totalIndices = 0
        for i, num in enumerate(nums):
            runningCt += num
            totalIndices += i + 1
        return totalIndices - runningCt
