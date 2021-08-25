from typing import List

#TLE on LC due to no lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.backtrack(s, wordDict, 0, {})

    def backtrack(self, s, word_dict, start_idx, memo):
        if start_idx == len(s):
            return True
        if start_idx in memo:
            return True
        ok = False
        for word in word_dict:
            if start_idx in memo or s[start_idx:].startswith(word):
                if self.backtrack(s, word_dict, start_idx + len(word), memo):
                    ok = True
                    break
        memo[start_idx] = ok
        return memo[start_idx]
a = "leetcode"
a_b = ["leet","code"]
#f
b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
b_b = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
#t
c = "catsandog"
c_c = ["cats","dog","sand","and","cat"]

wb = Solution()
wb.wordBreak(c, c_c)
print(wb.wordBreak(b, b_b))