class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        summ = sum(chalk)
        k %= summ
        ans = 0
        i = 0
        while k>0:
            if k - chalk[i] <0:
                return i
            else:
                k -= chalk[i]
            if i +1 < len(chalk):
                i+=1
            else:
                i = 0
        return i