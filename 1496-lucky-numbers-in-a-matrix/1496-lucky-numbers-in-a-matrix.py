class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minn = [min(matrix[i]) for i in range(len(matrix))]
        maxx = [max([matrix[i][j] for i in range(len(matrix))]) for j in range(len(matrix[0]))]
        ans = []
        for elem1 in minn:
            for elem2 in maxx:
                if elem1 == elem2:
                    ans.append(elem1)
                    break
        return ans