import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    return heapq.nlargest(k, heap)[-1]