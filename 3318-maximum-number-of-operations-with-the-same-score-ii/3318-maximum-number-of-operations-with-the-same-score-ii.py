class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2 or len(nums) ==3:
            return 1
        """del first two """
        n1 = nums[0] + nums[1]
        nums1 = nums[2:] 
        """del first one and last one"""
        n2 = nums[0] + nums[-1]
        nums2 = nums[1:-1]
        """del last two """
        n3 = nums[-1] + nums[-2]
        nums3 = nums[:-2]
        """create three dictionaries"""
        f = {n1:{}, n2:{}, n3:{}}
        """def the func with input type: (list, num)"""
        def sol(l, n):
            pos1, pos2, pos3 = 0,0,0
            if len(l)==2 and sum(l)==n:
                return 1
            if len(l) == 3:
                if sum(l[:2])==n or sum(l[1:])==n or l[0]+l[2]==n:
                    return 1
                else:
                    return 0
            
            if l[0] + l[1] == n and tuple(l[2:]) in f[n]:
                pos1 = f[n][tuple(l[2:])]+1
            elif l[0] + l[1] == n:
                f[n][tuple(l[2:])] = sol(l[2:], n)
                pos1 = f[n][tuple(l[2:])]+1

            if l[0] + l[-1] ==n and tuple(l[1:-1]) in f[n]:
                pos2 = f[n][tuple(l[1:-1])]+1
            elif l[0]+l[-1] == n:
                f[n][tuple(l[1:-1])] = sol(l[1:-1], n)
                pos2 = f[n][tuple(l[1:-1])]+1

            if l[-1] + l[-2] ==n and tuple(l[:-2]) in f[n]:
                pos3 = f[n][tuple(l[:-2])]+1
            elif l[-1] + l[-2] == n:
                f[n][tuple(l[:-2])] = sol(l[:-2], n)
                pos3 = f[n][tuple(l[:-2])]+1
            return max(pos1, pos2, pos3)
        return max(sol(nums1, n1), sol(nums2, n2), sol(nums3, n3))+1
        