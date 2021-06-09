def longestPalindrome(self, s):
    dp = [[0] * len(s) for _ in range(len(s))]
    t = ""
    for i in range(len(s)):
        dp[i][i] = 1
        t = s[i]
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j] and (j - i == 1 or dp[i + 1][j - 1] == 1):
                dp[i][j] = 1
                if len(t) < len(s[i:j + 1]):
                    t = s[i:j + 1]
    return t

print(longestPalindrome('', 'babad'))
print(longestPalindrome('', 'cbbd'))
print(longestPalindrome('', 'a'))
print(longestPalindrome('', 'ac'))
