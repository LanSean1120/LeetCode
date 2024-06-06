class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = str()
        mnum = num//1000
        num -= mnum*1000
        cnum = num//100
        num -= cnum*100
        xnum = num//10
        num -= xnum*10
        inum = num
        ans += mnum*"M"
        if cnum == 9:
            ans += "CM"
        elif cnum == 4:
            ans += "CD"
        elif cnum >=5:
            ans += "D"
            ans += (cnum-5)*"C"
        else:
            ans += cnum*"C"

        if xnum == 9:
            ans += "XC"
        elif xnum == 4:
            ans += "XL"
        elif xnum >=5:
            ans += "L"
            ans += (xnum-5)*"X"
        else:
            ans += xnum*"X"
        
        if inum == 9:
            ans += "IX"
        elif inum == 4:
            ans += "IV"
        elif inum >=5:
            ans += "V"
            ans += (inum-5)*"I"
        else:
            ans += inum*"I"
        return ans
