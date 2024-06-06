class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        N=n
        ans = []
        l=[]
        for i in range(1,n+1):
            l.append(i)
        k=k-1
        while len(l)>=1:
            m=1
            for i in range(1,n):
                m*=i
            
            ans.append(l[k//m])
            del l[k//m]
            n-=1
            k = k%m
        Ans = ""
        
        for i in range(len(ans)):
            Ans +=str(ans[i])
        return Ans