class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = ""
        for i in range(len(s)):
            if s[i] in ["-", "+"] and ans == "":
                ans += s[i]
            
            elif s[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9","0"] and ans in ["", "+", "-"]:
                ans += s[i]
            elif s[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] and ans[-1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                ans += s[i]
            elif s[i] not in [' ', "-", "+", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] and ans == "":
                break
            elif s[i] == " " and ans == "":
                continue
            else: break

        if ans =="" or ans == "-" or ans == "+":
            ans =0
        elif ans[0] == "-":
            Ans =""
            for i in range(1, len(ans)):
                if ans[i]=="0":
                    continue
                else:
                    Ans = ans[i:]
                    break
            if Ans == "":
                ans =0
            else: ans = -1*int(Ans)
        elif ans[0] == "+":
            Ans =""
            for i in range(1, len(ans)):
                if ans[i]=="0":
                    continue
                else:
                    Ans = ans[i:]
                    break
            if Ans == "":
                ans =0
            else: ans = int(Ans)
        else: 
            Ans =""
            for i in range(0, len(ans)):
                if ans[i]== "0":
                    continue
                else:
                    Ans = ans[i:] 
                    break
            if Ans == "":
                ans =0
            else: ans = int(Ans)

        if ans > 2**(31)-1:
            return  2**(31)-1
        elif ans < -1*2**(31):
            return -1*2**(31)
        else: return ans
            
            
