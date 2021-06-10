import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        start = 0
        chars = {}
        #print('res, start, i, chars')
        for i, c in enumerate(s):
            if c in chars:
                start = max(start, chars[c] + 1)
                # No need to recreate the table after each collision
                #chars = {key:value for key, value in chars.items() if value > start}
            #print(s[start:i+1])
            res = max(res, i + 1 - start)
            chars[c] = i
            #print(res, start, i, chars)
        return res

print(
    # 1
    Solution.lengthOfLongestSubstring("", " "),
    # 3
    Solution.lengthOfLongestSubstring("", "dvdf"),
    # 2
    Solution.lengthOfLongestSubstring("", "abba"),
    # 3
    Solution.lengthOfLongestSubstring("", "acbca")
)