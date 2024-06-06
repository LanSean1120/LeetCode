class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
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
        return ans