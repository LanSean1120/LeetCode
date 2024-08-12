class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        mat = []
        for row in grid:
            curr = [[], [], []]
            for i in range(len(row)):
                if row[i] == " ":
                    curr[0] += [0,0,0]
                    curr[1] += [0,0,0]
                    curr[2] += [0,0,0]
                elif row[i] == "/":
                    curr[0] += [0,0,1]
                    curr[1] += [0,1,0]
                    curr[2] += [1,0,0]
                else:
                    curr[0] += [1,0,0]
                    curr[1] += [0,1,0]
                    curr[2] += [0,0,1]
            mat += curr
        
        representives = {}
        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j] == 0:
                    representives[(i, j)] = (i, j)

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

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] ==0:
                    if j+1 < len(mat) and mat[i][j+1] == 0:
                        connect((i, j), (i, j+1))
                    if j-1>=0 and mat[i][j-1] == 0:
                        connect((i, j-1), (i, j))
                    if i+1 < len(mat) and mat[i+1][j] ==0:
                        connect((i, j), (i+1, j))
                    if i-1 >=0 and mat[i-1][j] == 0:
                        connect((i-1, j), (i, j))
        seen = set()
        ans = 0
        for key in representives.keys():
            if find(key) not in seen:
                ans+=1
                seen.add(find(key))
        return ans