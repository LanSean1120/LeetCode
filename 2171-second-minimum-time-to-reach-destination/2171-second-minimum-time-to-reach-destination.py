class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        stack = deque([1])
        count = 0
        res = -1
        visited = defaultdict(list)

        while stack:
            m = len(stack)
            finds = False
            for i in range(m):
                curr = stack.popleft()
                if curr == n:
                    if res !=-1:
                        res = count
                        finds = True
                    res = count
                for nei in adj[curr]:
                    vis = visited[nei]
                    if len(vis)==0 or (len(vis)==1 and vis[0] !=count):
                        stack.append(nei)
                        visited[nei].append(count)
            count +=1
            if finds:
                break


        ans = 0
        while res>0:
            if (ans//change)%2==1:
                ans += change - (ans%change)
            ans += time
            res-=1
        return ans