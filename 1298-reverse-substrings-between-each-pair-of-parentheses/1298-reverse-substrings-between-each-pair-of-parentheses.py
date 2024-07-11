class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = deque()
        parentheses = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                temp = stack.pop()
                parentheses.append([temp, i])
            else:
                continue
        for l,k in parentheses:
            s = s[:l] + s[l:k+1][::-1] + s[k+1:]

        ans = ''
        for char in s:
            if char != "(" and char != ")":
                ans += char
        return ans