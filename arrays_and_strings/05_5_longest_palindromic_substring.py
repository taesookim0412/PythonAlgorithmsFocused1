class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = -1
        longestStr = ""
        for i in range(len(s)):
            L = R = i
            case = 0
            cases = [False, False]
            try:
                while L >= 0 and R < len(s) and (s[L] == s[R] or cases != [True, True]):
                    res = self.compare(s, L, R)
                    if res:
                        cases = [False, False]
                        if R - L > longest:
                            longest = R - L
                            longestStr = s[L:R + 1]
                    if (case + 1) % 2 == 0:
                        L -= 1
                        cases[1] = True
                    else:
                        R += 1
                        cases[0] = True

                    case += 1
            except Exception as e:
                print(L, R, s)
        return longestStr

    # returns a length
    def compare(self, s, start, end):
        return s[start:end + 1] == s[start:end + 1][::-1]

    # brute force (TLE)
    # def longestPalindrome(self, s: str) -> str:
    #     strList = list(s)
    #     longest = 0
    #     longestStrList = []
    #     for i in range(len(s)):
    #         for j in range(i, len(s) + 1):
    #             potStr = strList[i:j]
    #             if potStr == list(reversed(potStr)):
    #                 if len(potStr) > longest:
    #                     longest = len(potStr)
    #                     longestStrList = potStr
    #     return ''.join(longestStrList)