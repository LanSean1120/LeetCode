from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        T = distanceThreshold
        inf = float('inf')
        dis_mat = [[0 if i == j else inf for i in range(n)] for j in range(n)]
        
        # Set direct connections
        for edge in edges:
            dis_mat[edge[0]][edge[1]] = edge[2]
            dis_mat[edge[1]][edge[0]] = edge[2]
        
        # Floyd-Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dis_mat[i][k] < inf and dis_mat[k][j] < inf:  # Avoid overflow
                        dis_mat[i][j] = min(dis_mat[i][j], dis_mat[i][k] + dis_mat[k][j])
        
        ans = -1
        count = n
        
        for i in range(n):
            cur_count = sum(1 for j in range(n) if dis_mat[i][j] <= T)
            if cur_count <= count:
                ans = i
                count = cur_count
                
        return ans
