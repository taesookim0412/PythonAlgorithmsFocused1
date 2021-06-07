from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[(i + len(nums)//2) % len(nums)] == nums[i]:
                return nums[i]
        return -1
    # def majorityElement(self, nums: List[int]) -> int:
    #     cts = Counter(nums)
    #     sorted_cts = sorted(cts.items(), key=lambda x: x[1])
    #     return sorted_cts[-1][0]