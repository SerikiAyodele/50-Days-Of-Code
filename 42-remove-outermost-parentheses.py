class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ''
        string = ''
        stack = []
        
        for c in s:
            if c == '(':
                stack.append(c)
            else: # c == ')'
                if stack and stack[-1]:
                    stack.pop()
            string += c
            if not stack:
                res += string[1:-1]
                string = ''
        return res