from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = list(sorted(intervals + [newInterval]))
        if len(intervals) == 0: return []
        res = [intervals[0]]
        for i, interval in enumerate(intervals):
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res
