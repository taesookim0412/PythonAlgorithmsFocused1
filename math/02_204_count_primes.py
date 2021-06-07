from collections import Counter


class Solution:
    def countPrimes(self, n: int) -> int:
        dp = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            for j in range(i, (n//i) + 1):
                idx = i*j
                print(i,j,n,idx)
                if dp[idx] != -1:
                    dp[idx] = -1
        return Counter(dp[2:-1])[1]
    #brute force
    # def countPrimes(self, n: int) -> int:
    #     ct = 0
    #     for i in range(2, n):
    #         for j in range(2, i):
    #             if i % j == 0:
    #                 break
    #         else:
    #             ct += 1
    #     return ct