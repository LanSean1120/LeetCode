class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = [[0,i] for i in range(n)]
        for i in range(len(roads)):
            d[roads[i][0]][0]+=1
            d[roads[i][1]][0]+=1
        d.sort()
        for i in range(n):
            d[i][0] = i+1

        D = {d[i][1]:d[i][0] for i in range(len(d))}
        ans = 0

        for i in range(len(roads)):
            ans += D[roads[i][0]]+D[roads[i][1]] 
        return ans