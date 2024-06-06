class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        mx_len = 0
        f = {}
        for i, char in enumerate(s):
            if char in f and start <= f[char]:
                start = f[char]+1
            else:
                mx_len = max(mx_len, i-start+1)
            f[char] = i
        return mx_len
        