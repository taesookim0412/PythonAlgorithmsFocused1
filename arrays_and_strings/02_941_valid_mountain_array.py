from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        descending = False
        maxNum = -1
        for i in range(1, len(arr)):
            if arr[i - 1] == arr[i]:
                return False
            if arr[i - 1] < arr[i] and descending:
                return False
            elif arr[i - 1] > arr[i]:
                descending = True
            maxNum = max(maxNum, arr[i])
        return arr[0] < maxNum and maxNum > arr[-1]
