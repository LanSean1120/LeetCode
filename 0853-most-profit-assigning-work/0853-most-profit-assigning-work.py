class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        sheet = [[profit[i], difficulty[i]] for i in range(len(profit))]
        sheet.sort()
        sheet = sheet[::-1]
        mx = 0
        res = 0
        worker.sort()
        worker = worker[::-1]
        for i in range(len(worker)):
            check = res
            for j in range(mx, len(sheet)):
                if worker[i]>=sheet[j][1]:
                    res += sheet[j][0]
                    mx = j
                    break
            if check == res:
                break
        return res
                