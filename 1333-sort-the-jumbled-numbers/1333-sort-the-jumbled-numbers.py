class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapp(x):
            x = str(x)
            res = ""
            for i in range(len(x)):
                res += str(mapping[int(x[i])])
            return int(res)
        
        d = {n: (mapp(n), i) for i, n in enumerate(nums)}
        return sorted(nums, key = lambda x:d[x])
