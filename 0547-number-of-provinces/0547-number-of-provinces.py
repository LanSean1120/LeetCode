class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        representives = {i:i for i in range(len(isConnected))}
        def find(x):
            if x==representives[x]:
                return x
            else:
                return find(representives[x])
        def combine(a, b):
            a = find(a)
            b = find(b)
            if a==b:
                return
            else:
                representives[b] = a
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i!=j:
                    if isConnected[i][j] ==1:
                        combine(i, j)
        ans_set = set()
        for i in range(len(isConnected)):
            ans_set.add(find(i))
        return len(ans_set)
