from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        binaries = [0 for _ in range(n+1)]
        for n in range(n+1):
            i = n
            while n >= 1:
                binaries[i] += n % 2
                n //= 2
        return binaries