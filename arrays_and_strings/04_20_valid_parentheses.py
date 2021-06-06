class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = {0:'(', 1:'{', 2:'['}
        closed_brackets = {')':0, '}':1, ']':2}
        for ch in s:
            #if opener
            if ch not in closed_brackets:
                stack.append(ch)
            #if closer
            else:
                if len(stack) == 0 or stack[-1] != open_brackets[closed_brackets[ch]]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0