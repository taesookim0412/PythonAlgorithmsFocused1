from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     founds = set()
    #     for num in nums:
    #         if num in founds:
    #             return True
    #         founds.add(num)
    #     return False