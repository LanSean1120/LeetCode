class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ok_time = 0
        total_time = 0

        for i in range(len(customers)):
            if ok_time <= customers[i][0]:
                ok_time = customers[i][0] + customers[i][1]
                total_time += customers[i][1]
            else:
                ok_time += customers[i][1]
                total_time += ok_time - customers[i][0]
        return total_time/len(customers)