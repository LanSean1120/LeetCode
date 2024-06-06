class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words[0])
        m = len(words)
        ans = []
        if len(s) < n*m:
            return []
        for i in range(len(s)-n*m+1):
            if s[i:i+n] in words:
                if sorted([s[i+j:i+j+n] for j in range(0, n*m, n)]) == sorted(words):
                    ans.append(i)
        return ans

