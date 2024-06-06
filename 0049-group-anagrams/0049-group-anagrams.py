class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for i in range(len(strs)):
            if tuple(sorted([char for char in strs[i]])) not in ans:
                ans[tuple(sorted([char for char in strs[i]]))] = [i]
            else:
                ans[tuple(sorted([char for char in strs[i]]))].append(i)
        l = []
        for i in ans:
            l.append([strs[k] for k in ans[i]])
        return l