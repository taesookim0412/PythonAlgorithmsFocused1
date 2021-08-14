from typing import List

def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    l, r = 0, len(arr) -1
    while l < r:
        total = arr[l] + arr[r]
        if total > target:
            r -= 1
        elif total < target:
            l += 1
        elif total == target:
            return [l, r]
    return []

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum_sorted(arr, target)
    print(' '.join(map(str, res)))
