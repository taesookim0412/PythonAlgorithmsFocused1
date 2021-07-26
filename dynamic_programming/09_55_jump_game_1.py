from typing import List


#recursive, not one pass (refer to javascript)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.helper(nums, nums[0], 0)

    def helper(self, nums, currentNum, idx):
        if idx >= len(nums) - 1:
            return True
        for i in range(currentNum):
            amountToJump = i + 1
            newIndex = idx + amountToJump
            if self.helper(nums, nums[newIndex], newIndex):
                return True
        return False
