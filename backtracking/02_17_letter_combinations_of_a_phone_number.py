class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.res = []
        self.digits = digits
        self.charMap = {2: 'abc',
                        3: 'def',
                        4: 'ghi',
                        5: 'jkl',
                        6: 'mno',
                        7: 'pqrs',
                        8: 'tuv',
                        9: 'wxyz',
                        '2': 'abc',
                        '3': 'def',
                        '4': 'ghi',
                        '5': 'jkl',
                        '6': 'mno',
                        '7': 'pqrs',
                        '8': 'tuv',
                        '9': 'wxyz'}
        self.backtrack()
        return self.res

    def backtrack(self, letters=[], digit_idx=0, char_idx=0):
        if len(letters) == len(self.digits):
            self.res.append(''.join(letters))
            return
        for i in range(digit_idx, len(self.digits)):
            digit = self.digits[i]
            for j in range(char_idx, len(self.charMap[digit])):
                digit_char = self.charMap[digit][j]
                self.backtrack(letters + [digit_char], i + 1, 0)
