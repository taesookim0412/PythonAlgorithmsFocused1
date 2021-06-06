class Solution:
    dp = []
    def climbStairs(self, n: int) -> int:
        if len(self.dp) == 0:
            self.dp = [0 for _ in range(n+1)]
        if n == 2:
            return 2
        elif n == 1:
            return 1
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
        return self.dp[n]