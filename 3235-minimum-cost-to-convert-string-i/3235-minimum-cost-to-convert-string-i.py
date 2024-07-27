class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf = float("inf")
        mat = [[0 if i==j else inf for i in range(26)] for j in range(26)]

        n = len(cost)

        for i in range(n):
            mat[ord(original[i])-97][ord(changed[i])-97] = min(cost[i], mat[ord(original[i])-97][ord(changed[i])-97])

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        res = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                res += mat[ord(source[i])-97][ord(target[i])-97]

        return res if res!=inf else -1