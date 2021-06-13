from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sCtr = Counter(s)
        tCtr = Counter(t)
        ctrDiff = tCtr - sCtr
        if len(ctrDiff) != 0 and max((ctrDiff).values()) > 0:
            return ""
        requiredChars = Counter(t)
        res_str = s
        for i in range(len(s)):
            ctr = Counter(s[:len(s) - i])
            for j in range(i+1):
                #window = s[j:len(s) + j - i]
                if j != 0:
                    ctr[s[j-1]] -= 1
                    ctr[s[len(s)+j-i-1]] += 1
                reqDifferences = requiredChars - ctr
                if len(reqDifferences) == 0 or max(reqDifferences.values()) <= 0:
                    res_str = min(res_str, s[j:len(s) + j - i], key=len)
        return res_str