from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1: return nums[-1]
        houses = [
            nums[1:],
            nums[:-1]
        ]
        res = 0
        for house in houses:
            dp = [0 for _ in range(len(house) + 2)]
            for i in range(len(house)):
                dp[i + 2] = max(dp[i + 1], dp[i] + house[i])
            res = max(res, dp[-1])
        return res
