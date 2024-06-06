class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s+" "
        start = 0
        end=1
        ans = ""
        while end<len(s):
            if end==len(s)-1:
                if end!=" ":
                    ans = s[start:end]+ans
                    end+=1
                    continue
            if s[start]==" ":
                start+=1
                end+=1
                continue
            elif s[end]!=" ":
                end+=1
                continue
            else:
                ans = s[start: end]+ans
                ans = " "+ans
                start = end+1
                end=start+1
        i=0
        while ans[i]==" ":
            i+=1
        ans = ans[i:]
        return ans
            
        