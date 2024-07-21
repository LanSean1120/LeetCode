class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        ans = [[0 for i in range(k)] for j in range(k)]
        row_con = defaultdict(list)
        for a, b in rowConditions:
            row_con[b].append(a)
        col_con = defaultdict(list)
        for l, r in colConditions:
            col_con[r].append(l)
        
        def topoHelper(i:int, adj: dict, stack, visited, recStack):
            visited[i-1] = True
            recStack[i-1] = True
            for j in adj[i]:
                if not visited[j-1]:
                    if topoHelper(j, adj, stack, visited, recStack):
                        return True
                elif recStack[j-1]:
                    return True
            recStack[i-1] = False
            stack.append(i)
            return False

        row = deque()
        visited = [False for i in range(k)]
        recStack = [False for i in range(k)]
        for i in range(1, k+1):
            if not visited[i-1]:
                if topoHelper(i, row_con, row, visited, recStack):
                    return []
        row = list(row)
        col = deque()
        visited = [False]*k
        recStack = [False for i in range(k)]
        for i in range(1, k+1):
            if not visited[i-1]:
                if topoHelper(i, col_con, col, visited, recStack):
                    return []
        col = list(col)
        index = defaultdict(list)
        for i in range(len(row)):
            index[row[i]].append(i)
        for i in range(len(col)):
            index[col[i]].append(i)
        
        for key in index:
            i, j = index[key][0], index[key][1]
            ans[i][j] = key
        return ans




