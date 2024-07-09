class Solution:
    def longestPalindrome(self, s: str) -> str:
        candidates = [s[0]]
        for i in range(len(s)):
            j = 0
            while i+j<len(s) and i-j >= 0:
                if s[i+j] != s[i-j]:
                    if i-j+1 >= i+j-1 :
                        break
                    candidates.append(s[i-j+1:i+j-1 +1])
                    break
                if (i+j == len(s)-1 or i-j == 0) and s[i+j] == s[i-j]:
                    candidates.append(s[i-j:i+j +1])
                j+=1

        for k in range(len(s)-1):
            if s[k] == s[k+1]:
                j = 0
                while k+1+j <len(s) and k-j >= 0:
                    if s[k+1+j] != s[k-j]:
                        candidates.append(s[k-j+1: k+1+j-1+1])
                        break
                    if (k+1+j == len(s)-1 or k-j==0) and s[k+1+j] == s[k-j]:
                        candidates.append(s[k-j:k+1+j+1])
                    j+=1
        ans = candidates[0]
        for elem in candidates:
            if len(elem) > len(ans):
                ans = elem
        return ans
