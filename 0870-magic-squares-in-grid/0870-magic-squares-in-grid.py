class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def check(mat):
            nums = [mat[i][j] for i in range(3) for j in range(3)]
            if set(nums)!=set([1,2,3,4,5,6,7,8,9]):
                return False
            summ = sum(mat[0])
            for i in range(3):
                if sum(mat[i])!=summ:
                    return False
                if sum([mat[j][i] for j in range(3)]) != summ:
                    return False
            if mat[0][0] + mat[1][1] + mat[2][2] !=summ:
                return False
            if  mat[0][2] + mat[1][1] + mat[2][0] !=summ:
                return False
            return True
        row = len(grid)
        col = len(grid[0])
        ans = 0
        for i in range(row):
            for j in range(col):
                if i+3<=row and j+3<=col:
                    if check([row[j:j+3] for row in grid[i:i+3]]):
                        ans+=1
        return ans
