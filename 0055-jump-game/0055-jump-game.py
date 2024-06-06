class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        intervals = [[i, i+nums[i]] for i in range(len(nums))]
        ans =[]
        for i in range(len(intervals)):
            finds = False
            if ans == []:
                ans.append(intervals[i])
                continue
            for j in range(len(ans)):
                if intervals[i][0]<=ans[j][1]:
                    ans[j][1] = max(intervals[i][1], ans[j][1])
                    finds = True
                    break
            if finds:
                continue
            ans.append(intervals[i])
        return True if len(ans)==1 else False