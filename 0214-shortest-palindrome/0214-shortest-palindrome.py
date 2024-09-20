class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        temp = s[::-1]
        n = len(s)
        for i in range(1, n):
            if s[:n-i] == temp[i:]:
                return temp[:i] + s
        return temp + s