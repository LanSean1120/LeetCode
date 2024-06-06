class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows ==1:
            return s
        n = 2*numRows - 2
        l = [s[i::n] for i in range(n)]
        ans = ''
        ll = ["" for i in range(numRows)]
        ll[0] = l[0]
        ll[numRows-1] = l[numRows-1]

        for i in range(1, numRows-1):
            min_len = min(len(l[i]), len(l[n-i]))
            for j in range(min_len):
                ll[i] += l[i][j] + l[n-i][j]
            ll[i] += l[i][min_len:] + l[n-i][min_len:]
        
        for i in range(len(ll)):
            ans += ll[i]
        return ans


        
            

        