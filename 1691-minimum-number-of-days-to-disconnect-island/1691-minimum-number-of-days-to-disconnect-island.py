class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def disconnected(mat):
            representives = {}
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    if mat[i][j] == 1:
                        representives[(i, j)] = (i, j)
            def find(a):
                if representives[a] == a:
                    return a
                else:
                    return find(representives[a])
            def union(a, b):
                a = find(a)
                b = find(b)
                if a==b:
                    return 
                else:
                    representives[b] = a

            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    if mat[i][j] == 1:
                        if j+1 < len(mat[i]) and mat[i][j+1]==1:
                            union((i, j), (i, j+1))
                        if j-1 >=0 and mat[i][j-1] == 1:
                            union((i, j-1), (i, j))
                        if i-1 >=0 and mat[i-1][j] == 1:
                            union((i-1, j), (i, j))
                        if i+1 < len(mat) and mat[i+1][j]==1:
                            union((i, j), (i+1, j))
            
            seen = set()
            res = 0
            for key in representives.keys():
                if find(key) not in seen:
                    res+=1
                    seen.add(find(key))
            
            if res ==1:
                return False
            else:
                return True
       

        if disconnected(grid):
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    grid[i][j]-=1
                    if disconnected(grid):
                        return 1
                    grid[i][j] += 1
                    continue
                else:
                    continue
        return 2

