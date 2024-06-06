class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        for i in range(1, len(str(x))):
            if str(x)[-i]==0:
                x = x/10
            else: break
        if x<0:
            ans = -1*int(str(-1*x)[::-1])
        else: ans = int(str(x)[::-1])
        if ans > 2**(31)-1 or ans < -1*2**(31):
            return 0
        else: return ans