class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0 for i in range(n)] for j in range(n)]
        num =1
        up =0
        down =n-1
        N=n
        while n>2:
            for i in range(up, down+1):
                ans[up][i] = num
                num+=1

            for j in range(up+1,down):
                ans[j][down]=num
                num+=1
            for k in range(0,down+1-up):
                ans[down][down-k] = num
                num+=1
            for l in range(1,down-up):
                ans[down-l][up]=num
                num+=1
            up+=1
            down-=1
            n-=2


        if n == 2:
            ans[N/2-1][N/2-1]=num
            num+=1
            ans[N/2-1][N/2]=num
            num+=1
            ans[N/2][N/2]=num
            num+=1
            ans[N/2][N/2-1]=num
        elif n==1:
            ans[N/2][N/2]=num

        
        return ans
        