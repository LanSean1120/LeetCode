class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def sol(l):
            ans = []
            if len(l) ==1:
                return [l]
            for i in range(len(l)):
                ans += [[l[i]] + char for char in sol(l[:i]+l[i+1:])]
            return ans
            
        return sol(nums)

                

        