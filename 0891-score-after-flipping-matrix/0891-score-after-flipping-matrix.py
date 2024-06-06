class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if grid[i][0]==1:
                continue
            else:
                for j in range(len(grid[i])):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
        for i in range(len(grid[0])):
            temp = [grid[k][i] for k in range(len(grid))]
            if temp.count(1) <= len(grid)//2:
                for k in range(len(grid)):
                    if grid[k][i] == 0:
                        grid[k][i] = 1
                    else:
                        grid[k][i] = 0
        ans = 0
        for i in range(len(grid)):
            grid[i] = grid[i][::-1]

        for i in range(len(grid)):
            for k in range(len(grid[i])):
                ans += grid[i][k]*2**k

        return ans