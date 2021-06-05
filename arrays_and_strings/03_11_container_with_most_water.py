from typing import List


class Solution:
    #Two pointer
    #The proof states that if there is an answer, and the number at
    #num[l + _a] > num[l], then the number at num[r] will decrease
    #and calculate num[r] to num[r - _b] accordingly from l to r anyways.
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(height) - 1
        while l < r:
            maxArea = max(maxArea, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
    #TLE
    # def maxArea(self, height: List[int]) -> int:
    #     maxArea = 0
    #     for i, num in enumerate(height):
    #         for j in range(i+1):
    #             maxArea = max(
    #             maxArea,
    #             (i - j) * min(num, height[j]) )
    #     return maxArea