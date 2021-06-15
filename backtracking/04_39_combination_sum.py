from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res, self.candidates, self.target = [], candidates, target
        self.backtrack()
        return self.res

    def backtrack(self, vals=[], start=0):
        valSum = sum(vals)
        if valSum == self.target:
            self.res.append(vals)
            return
        elif valSum > self.target:
            return
        for i in range(start, len(self.candidates)):
            self.backtrack(vals + [self.candidates[i]], i)
