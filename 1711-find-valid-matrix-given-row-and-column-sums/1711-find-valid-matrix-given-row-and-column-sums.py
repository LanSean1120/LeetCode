class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ans = [["_" for i in range(len(colSum))] for j in range(len(rowSum))]
        R = len(rowSum)
        C = len(colSum)
        while rowSum.count("_")!= R and colSum.count("_") != C:
            c, r = 0, 0
            for i in range(R):
                if rowSum[i] != "_":
                    if rowSum[r] == "_":
                        r = i
                    if rowSum[i] < rowSum[r]:
                        r = i

            for j in range(C):
                if colSum[j] != "_":
                    if colSum[c] == "_":
                        c = j
                    if colSum[j] < colSum[c]:
                        c = j

            if rowSum[r] <= colSum[c]:
                for i in range(C):
                    if i == c:
                        ans[r][c] = rowSum[r]
                    elif ans[r][i] == "_":
                        ans[r][i] = 0
                colSum[c] -= rowSum[r]
                rowSum[r] = "_"
                
            else:
                for i in range(R):
                    if i == r:
                        ans[r][c] = colSum[c]
                    elif ans[i][c] == "_":
                        ans[i][c] = 0
                rowSum[r] -= colSum[c]
                colSum[c] = "_"
                
        return ans
