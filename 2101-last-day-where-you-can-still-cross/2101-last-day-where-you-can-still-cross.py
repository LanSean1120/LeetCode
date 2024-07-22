class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def neighbor(cell):
            i, j = cell
            res = []
            if i - 1 >= 1:
                res.append([i - 1, j])
            if i + 1 <= row:
                res.append([i + 1, j])
            if j - 1 >= 1:
                res.append([i, j - 1])
            if j + 1 <= col:
                res.append([i, j + 1])
            return res

        def check(n):
            blocked = set(map(tuple, cells[:n]))
            queue = deque([(1, i) for i in range(1, col + 1) if (1, i) not in blocked])
            visited = set(queue)
            
            while queue:
                curr_i, curr_j = queue.popleft()
                if curr_i == row:
                    return True
                for ni, nj in neighbor((curr_i, curr_j)):
                    if (ni, nj) not in blocked and (ni, nj) not in visited:
                        queue.append((ni, nj))
                        visited.add((ni, nj))
            return False
        
        left, right = 1, row * col
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        
        return left