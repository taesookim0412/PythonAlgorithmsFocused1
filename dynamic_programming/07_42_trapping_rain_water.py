from typing import List


class Solution:
    #O(n) with O(1) space
    # def trap(self, height: List[int]) -> int:
    #     l, r = 0, len(height) - 1
    #     leftMax, rightMax = height[l], height[r]
    #     waters = 0
    #     while l < r:
    #         if leftMax < rightMax:
    #             l += 1
    #             leftMax = max(leftMax, height[l])
    #             waters += leftMax - height[l]
    #         else:
    #             r -= 1
    #             rightMax = max(rightMax, height[r])
    #             waters += rightMax - height[r]
    #     return waters

    #O(n) with O(n) space (dp)
    def trap(self, height: List[int]) -> int:
        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]
        leftMax = 0
        rightMax = 0
        waters = 0
        for i in range(len(left_max)):
            left_max[i] = leftMax
            leftMax = max(leftMax, height[i])
        for i in range(len(right_max) -1, -1, -1):
            right_max[i] = rightMax
            rightMax = max(rightMax, height[i])
        minHeights = [0 for _ in range(len(height))]
        for i in range(len(height)):
            minHeights[i] = min(left_max[i], right_max[i])
        for i in range(len(height)):
            if height[i] < minHeights[i]:
                waters += minHeights[i] - height[i]
        return waters

print(
    Solution.trap('', [0,1,0,2,1,0,1,3,2,1,2,1])
)

