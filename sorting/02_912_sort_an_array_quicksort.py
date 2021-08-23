from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, l, r):
        if l < r:
            pi = self.partition(nums, l, r)
            self.quicksort(nums, l, pi - 1)
            self.quicksort(nums, pi + 1, r)

    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] < pivot:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1