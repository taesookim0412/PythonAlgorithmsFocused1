from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsetsSet = set()
        self.nums = nums
        self.backtrack([], 0)
        return self.subsetsSet

    def backtrack(self, vals, starting_i):
        self.subsetsSet.add(tuple(vals))
        for i in range(starting_i, len(self.nums)):
            self.backtrack(vals + [self.nums[i]], i + 1)