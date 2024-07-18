class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        representives = {(i, j):(i, j) for i in range(len(grid)) for j in range(len(grid[0]))}

        def find(a):
            if representives[a] == a:
                return a
            else:
                return find(representives[a])

        def connect(a, b):
            a = find(a)
            b = find(b)
            if a==b:
                return 
            else:
                representives[b] = a
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if i+1<len(grid) and grid[i+1][j]=="1":
                        connect((i, j), (i+1, j))
                    if j+1<len(grid[0]) and grid[i][j+1]=="1":
                        connect((i, j), (i, j+1))

                else:
                    representives[(i, j)] = 0

        seen = set()
        ans = 0
        for key in representives:
            if representives[key] !=0 and find(key) not in seen:
                ans+=1
                seen.add(find(key))

        return ans
        
