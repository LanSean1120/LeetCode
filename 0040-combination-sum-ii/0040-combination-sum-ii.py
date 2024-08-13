class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def sol(start: int, t: int):
            if t<0:
                return 
            if t==0:
                return [[]]
            
            res = []
            for i in range(start, len(candidates)):
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                candi = sol(i+1, t-candidates[i])
                if candi:
                    for cand in candi:
                        res.append([candidates[i]]+cand)
            return res
            
        
        return sol(0, target)
            