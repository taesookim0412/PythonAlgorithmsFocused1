import collections
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        twoSums = collections.defaultdict(int)
        res = 0
        for num1 in nums1:
            for num2 in nums2:
                twoSums[num1 + num2] += 1
        for num3 in nums3:
            for num4 in nums4:
                val = -1 * (num3 + num4)
                if val in twoSums:
                    res += twoSums.get(val, 0)
        return res
