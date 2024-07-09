class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        for i in range(len(s)):
            j = 0
            while i+j<len(s) and i-j >= 0:
                if s[i+j] != s[i-j]:
                    if i-j+1 >= i+j-1 :
                        break
                    if len(s[i-j+1:i+j-1 +1]) > len(ans):
                        ans = s[i-j+1:i+j-1 +1]
                    break
                if (i+j == len(s)-1 or i-j == 0) and s[i+j] == s[i-j]:
                    if len(s[i-j:i+j +1]) > len(ans):
                        ans = s[i-j:i+j +1]
                j+=1

        for k in range(len(s)-1):
            if s[k] == s[k+1]:
                j = 0
                while k+1+j <len(s) and k-j >= 0:
                    if s[k+1+j] != s[k-j]:
                        if len(s[k-j+1: k+1+j-1+1]) > len(ans):
                            ans = s[k-j+1: k+1+j-1+1]
                        break
                    if (k+1+j == len(s)-1 or k-j==0) and s[k+1+j] == s[k-j]:
                        if len(s[k-j:k+1+j+1]) > len(ans):
                            ans = s[k-j:k+1+j+1]
                    j+=1

        return ans
