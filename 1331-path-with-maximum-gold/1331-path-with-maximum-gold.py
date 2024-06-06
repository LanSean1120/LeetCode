class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = []
        
        def sol(r, c, visited, summ):
            if r>=len(grid) or r <0:
                return
            if c >=len(grid[0]) or c <0:
                return
            if [r,c] in visited:
                return
            if grid[r][c]==0:
                return
            visited.append([r,c])
            summ += grid[r][c]
            ans.append(summ)
            sol(r+1, c, visited, summ)
            sol(r, c+1, visited, summ)
            sol(r-1, c, visited, summ)
            sol(r, c-1, visited, summ)
            visited.pop()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                sol(i, j, [], 0)
        return max(ans) if ans !=[] else 0

            
            
        