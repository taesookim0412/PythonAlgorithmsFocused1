from typing import List

def rob(self, nums: List[int]) -> int:
    dp = [[0 for _ in range(len(nums)+2)] for _ in range(len(nums)+2)]
    for i in range(len(nums)):
        for j in range(i+1):
            dp[i+2][j+2] = max(
                max(dp[i+1][j+1], nums[j]),
                dp[i][j] + nums[j]
            )
    # print(dp)
    return dp[-1][-1]

print(rob(0, [2,7,9,3,1]))