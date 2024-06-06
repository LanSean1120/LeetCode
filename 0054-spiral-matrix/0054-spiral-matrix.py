class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        mat = matrix
        while min(len(mat), len(mat[0]))>2:
            for i in range(len(mat[0])):
                ans.append(mat[0][i])
            for j in range(1,len(mat)):
                ans.append(mat[j][-1])
            for k in range(1,len(mat[-1])):
                ans.append(mat[-1][len(mat[-1])-1-k])
            for l in range(1,len(mat)-1):
                ans.append(mat[len(mat)-1-l][0])
            mat_temp = mat
            mat = [[] for n in range(len(mat_temp)-2)]
            for i in range(1,len(mat_temp)-1):
                mat[i-1] = mat_temp[i][1:-1]
        if len(mat) == 2:
            ans +=mat[0]
            ans+=mat[1][::-1]
        elif len(mat[0])==2:
            ans.append(mat[0][0])
            for i in range(len(mat)):
                ans.append(mat[i][1])
            for j in range(1,len(mat)):
                ans.append(mat[len(mat)-j][0])
        elif len(mat) ==1:
            ans +=mat[0]
        elif len(mat[0]) ==1:
            for k in range(len(mat)):
                ans.append(mat[k][0])
        
        return ans


