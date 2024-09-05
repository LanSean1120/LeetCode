class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        resi = mean*(m+n) - sum(rolls)
        if resi <n or resi > 6*n:
            return []

        
        rest = resi %n
        ans = [resi//n]*n
        for i in range(rest):
            ans[i] += 1
        return ans