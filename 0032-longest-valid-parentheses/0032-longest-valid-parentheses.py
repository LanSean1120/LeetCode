class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = [ 0 for i in range(len(s))]
        stack = deque([])
        i = 0
        prev = deque([])
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                prev.append(i)
            if s[i] == ')':
                if stack:
                    temp = stack.pop()
                    if s[i] != temp:
                        l[i] += 1
                        last = prev.pop()
                        l[last] += 1
            
        
        count = 0
        ans = 0
        for i in range(len(l)):
            if l[i] == 1:
                count +=1
            else:
                ans = max(ans, count)
                count = 0
        ans = max(ans, count)
        return ans

                        
            
                