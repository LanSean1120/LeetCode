class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = ['(']
        l = ["(", ")"]
        for i in range(2*n-1):
            ans = [a+b for a in ans for b in l]
        
        Ans = []
        for i in range(len(ans)):
            if ans[i].count("(") != ans[i].count(")"):
                continue
            else:
                Ans.append(ans[i])
        
        ans1 = []
        for i in range(len(Ans)):
            n=0
            for j in range(len(Ans[i])):
                finds = True
                if Ans[i][j] == "(":
                    n+=1
                else:
                    n-=1
                if n<0:
                    finds = False
                    break
            if finds:
                ans1.append(Ans[i])


        return ans1

        
        
