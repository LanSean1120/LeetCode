class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if "e" not in s and "E" not in s:
            if s[0] == "+" or s[0] =="-":
                s=s[1:]
            if s == "." or s=="":
                return False
            if s.count(".")>=2:
                return False
            for i in range(len(s)):
                if s[i] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]:
                    return False
            return True


        sf = ""
        sb = ""
        for i in range(len(s)):
            if s[i] == "e" or s[i] == "E":
                sf = s[:i]
                sb = s[i+1:]
                break
        if sf == "" or sf == "+" or sf == "-" or sf == "." or sf.count(".")>1:
            return False
        if sf[0] == "+" or sf[0] == "-":
            sf = sf[1:]
        if sf == "" or sf == "+" or sf == "-" or sf == ".":
            return False
        for i in range(len(sf)):
            if sf[i] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]:
                return False
        """
        The other case
        """
        if sb == "":
            return False
        if sb[0]=="+" or sb[0]=="-":
            sb = sb[1:]
        if sb == "":
            return False
        for i in range(len(sb)):
            if sb[i] not in  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                return False
        return True





        