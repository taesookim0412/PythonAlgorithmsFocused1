import collections
from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    diffs = collections.defaultdict(int)
    for i, num in enumerate(nums):
        if target - num in diffs:
            return [diffs[target - num], i]
        else:
            diffs[num] = i
    return []
