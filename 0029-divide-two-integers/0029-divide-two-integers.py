class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans = 0
        if dividend/divisor>=0 and dividend/divisor <2**(31)-1:
            ans =dividend/divisor
        elif dividend/divisor >=2**(31)-1:
            ans = 2**(31)-1
        elif dividend/divisor < 0 and dividend%divisor==0  and dividend/divisor+1 > -1*2**(31):
            ans = dividend/divisor
        elif dividend/divisor < 0 and dividend%divisor!=0 and dividend/divisor+1 > -1*2**(31):
            return dividend/divisor+1
        else: ans = -1*2**(31)
        return ans