class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        f ={}
        def sol(l):
            if l==[]:
                return []
            if tuple(l) in f:
                return f[tuple(l)]
            pos = []
            for i in range(len(l)):
                temp = l[:i]+l[i+1:]
                for j in range(len(sol(temp))):
                    if sol(temp)[j] not in pos:
                        pos.append(sol(temp)[j])
            f[tuple(l)]= [l] + pos
            return f[tuple(l)]
        return sol(nums)+ [[]]