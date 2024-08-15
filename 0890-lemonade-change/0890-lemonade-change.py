class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        amount = {5:0, 10:0}
        for bill in bills:
            if bill==5:
                amount[5] += 1
            elif bill == 10:
                amount[5] -= 1
                amount[10] += 1
            else:
                if amount[10] > 0:
                    amount[10] -= 1
                    amount[5] -= 1
                else:
                    amount[5] -= 3
            if amount[5] <0:
                return False
        return True