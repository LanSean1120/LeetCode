class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        f={}
        def sol(n):
            if n == 0 or n==1:
                return []
            elif n == candidates[0]:
                f[candidates[0]] = [[candidates[0]]]
                return f[candidates[0]]
            if n in f:
                return f[n]
            temp = []
            for num in candidates:
                if num >n:
                    break
                if n == num:
                    temp.append([num])
                    continue
                else:
                    for i in range(len(sol(n-num))):
                        temp2 = sorted(sol(n-num)[i]+[num])
                        if temp2 not in temp:
                            temp.append(temp2)
            f[n] = temp
            return temp
        return sol(target)