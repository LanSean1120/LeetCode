class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        l=[0]
        for i in range(len(nums)):
            l.append(l[-1]+nums[i])
            l[-1] %= k
        
        d = defaultdict(list)
        for i in range(len(l)):
            d[l[i]].append(i)
        ans = 0
        def func(n):
            return n*(n-1)//2
        for key in d:
            elem = d[key]
            n = len(elem)
            if n>=2:
                ans += func(n)
            
        return ans
        
