class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] !=1:
            return False
        memo = {}
        def sol(i, k):
            if i == len(stones) -1:
                return True
            if (i, k) in memo:
                return memo[(i,k)]
            res = False
            for j in range(i+1,len(stones)):
                if stones[j] - stones[i] == k:
                    res = res or sol(j, k)
                if stones[j] - stones[i] == k-1:
                    res = res or sol(j, k-1)
                if stones[j] - stones[i] == k+1:
                    res = res or sol(j, k+1)
            memo[(i, k)] = res
            return res
        return sol(1,1)
