from typing import List


class Solution:
    #non graph
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return []
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i, interval in enumerate(intervals):
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res