class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k>1:
            l = [s[i] for i in range(len(s))]
            l.sort()
            ans = ""
            for i in range(len(l)):
                ans += l[i]
            return ans
        else:
            l = [s[i:]+s[:i] for i in range(len(s))]
            l.sort()
            return l[0]